"""The fixflags command."""

import requests
import json
from furl import furl
from pick import pick

from ppmutils.commands.base import Base
from ppmutils.commands.base import Style

import logging
logger = logging.getLogger('ppmutils')


class FixFlags(Base):
    """A fixflags command."""

    def run(self):
        """
        This method fixes an issue where a participant ended up with multiple
        PPM Flag resources that point to the same study. This will
        trim that count down to only one resources.

        :param url: The url to PPM's FHIR service
        :type url: str
        :returns: A list of PPM IDs that required cleanup
        :rtype: list
        """
        try:
            # Get patients first
            patients = self.query_bundle("Patient")
            for patient in patients:

                # Fetch everything for each one
                query = {"_id": patient["resource"]["id"], "_revinclude": ["ResearchSubject:individual", "Flag:subject"]}
                resources = self.query_bundle("Patient", query=query)

                # Get research subjects
                flags = [
                    r["resource"] for r in resources
                    if r["resource"]["resourceType"] == "Flag"
                    and next((iter(r["resource"].get("code", {}).get("coding", []))), {}).get("system") == "https://peoplepoweredmedicine.org/enrollment-status"
                ]

                # Ignore only one
                if len(flags) == 1:
                    continue

                # Figure out which ones to delete
                for flag in flags:

                    # Print it out
                    self.shell.print(f"--- Flag/{flag['id']} ---", style=Style.Info)
                    self.shell.print(f"\n{json.dumps(flag, indent=4)}\n", style=Style.Info)

                # Ask which one(s) to delete
                self.shell.yes_no(f"Remember which ones to delete! Ready to continue?", default=True)
                flag_ids = []
                while not flag_ids:
                    flag_ids = pick(
                        [r["id"] for r in flags],
                        "Select which Flag resources to delete ([space] to select multiple, [enter] to submit):",
                        multi_select=True
                        )

                    # Do not allow deleting them all
                    if len(flags) == len(flag_ids):
                        self.shell.print(f"Error: You cannot delete all resources!", style=Style.Error)
                        flag_ids = []

                # Delete the others
                for flag_id in flag_ids:
                    try:
                        # Make the request
                        delete_url = furl(self.url)
                        delete_url.path.segments.extend(["Flag", flag_id[0]])
                        if not self.shell.yes_no(f"Are you sure you want to DELETE -> {delete_url.url}?", default=False, style=Style.Warning):
                            continue
                        response = requests.delete(delete_url.url)
                        content = response.content
                        response.raise_for_status()

                        # Print it out
                        self.shell.print(f"Deleted Flag/{flag_id[0]} successfully", style=Style.Success)

                    except Exception as e:
                        self.shell.print(f"Error deleting Flag/{flag_id[0]}: {e}", style=Style.Error)
                        self.shell.print(f"FHIR response: {content}", style=Style.Error)

        except Exception as e:
            self.shell.print(f"Error: {e}", style=Style.Error)
