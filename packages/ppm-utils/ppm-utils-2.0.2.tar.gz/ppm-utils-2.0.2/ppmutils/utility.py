import json
import requests
from furl import furl
from pick import pick

from ppmutils.ppm import PPM
from ppmutils.fhir import FHIR



def yes_no(message, default=None):
    """
    Prompts the user with the given message and returns their response
    :param message: The message for the prompt
    :param default: The default answer that should be shown/returned
    :param style: The shell style/color
    :return: boolean
    """
    yes = ['yes', 'y', 'ye', '1', 'true', 't']
    no = ['no', 'n', '0', 'false', 'f']

    # Determine prompt text
    if default is not None:
        prompt = ' ({}): '.format(yes[0] if default else no[0])
    else:
        prompt = ': '

    while True:
        choice = input(message + prompt).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        elif not choice and default is not None:
            return default
        else:
            print('Please enter a valid response')


def query_bundle(url, resource_type, query=None):
    """
    This method will fetch all resources for a given type, including paged results.
    :param resource_type: FHIR resource type
    :type resource_type: str
    :param query: A dict of key value pairs for searching resources
    :type query: dict
    :return: A Bundle of FHIR resources
    :rtype: Bundle
    """
    # Build the URL.
    url_builder = furl(url)
    url_builder.path.add(resource_type)

    # Add query if passed and set a return count to a high number,
    # despite the server
    # probably ignoring it.
    url_builder.query.params.add("_count", 1000)
    if query is not None:
        for key, value in query.items():
            if type(value) is list:
                for _value in value:
                    url_builder.query.params.add(key, _value)
            else:
                url_builder.query.params.add(key, value)

    # Prepare the final URL
    query_url = url_builder.url

    # Collect them.
    total_bundle = None

    # The url will be set to none on the second iteration if all resources
    # were returned, or it will be set to the next page of resources if more exist.
    while query_url is not None:

        # Make the request.
        response = requests.get(query_url)
        response.raise_for_status()

        # Parse the JSON.
        bundle = response.json()
        if total_bundle is None:
            total_bundle = bundle
        elif bundle.get("total", 0) > 0:
            total_bundle["entry"].extend(bundle.get("entry"))

        # Check for a page.
        query_url = None

        for link in bundle.get("link", []):
            if link["relation"] == "next":
                query_url = link["url"]

    return bundle.get("entry", [])


def fix_multiple_research_subjects(url):
    """
    This method fixes an issue where a participant ended up with multiple
    PPM ResearchSubject resources that point to the same study. This will
    trim that count down to only one resources.

    :param url: The url to PPM's FHIR service
    :type url: str
    :returns: A list of PPM IDs that required cleanup
    :rtype: list
    """
    try:
        # Get patients first
        patients = query_bundle(url, "Patient")
        for patient in patients:

            # Fetch everything for each one
            query = {"_id": patient["resource"]["id"], "_revinclude": ["ResearchSubject:individual", "Flag:subject"]}
            resources = query_bundle(url, "Patient", query=query)

            # Get research subjects
            research_subjects = [
                r["resource"] for r in resources
                if r["resource"]["resourceType"] == "ResearchSubject"
                and r["resource"]["study"]["reference"].startswith(f"ResearchStudy/ppm-")
            ]

            # Ignore only one
            if len(research_subjects) == 1:
                continue

            # Figure out which ones to delete
            for research_subject in research_subjects:

                # Print it out
                print(f"ResearchSubject/{research_subject['id']}: \n\n{json.dumps(research_subject, indent=4)}\n\n")

            # Ask which one(s) to delete
            yes_no(f"Remember which ones to delete! Ready to continue?", default=True)
            research_subject_ids = []
            while not research_subject_ids:
                research_subject_ids = pick(
                    [r["id"] for r in research_subjects],
                    "Select which ResearchSubject resources to delete ([space] to select multiple, [enter] to submit):",
                    multi_select=True
                    )

                # Do not allow deleting them all
                if len(research_subjects) == len(research_subject_ids):
                    print(f"Error: You cannot delete all resources!")
                    research_subject_ids = []

            # Delete the others
            for research_subject_id in research_subject_ids:
                try:
                    # Make the request
                    delete_url = furl(url)
                    delete_url.path.segments.extend(["ResearchSubject", research_subject_id[0]])
                    if not yes_no(f"Are you sure you want to DELETE -> {delete_url.url}?", default=False):
                        continue
                    response = requests.delete(delete_url.url)
                    content = response.content
                    response.raise_for_status()

                    # Print it out
                    print(f"Deleted ResearchSubject/{research_subject_id[0]} successfully")

                except Exception as e:
                    print(f"Error deleting ResearchSubject/{research_subject_id[0]}: {e}")
                    print(f"FHIR response: {content}")

    except Exception as e:
        print(f"Error: {e}")


def fix_multiple_flags(url):
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
        patients = query_bundle(url, "Patient")
        for patient in patients:

            # Fetch everything for each one
            query = {"_id": patient["resource"]["id"], "_revinclude": ["ResearchSubject:individual", "Flag:subject"]}
            resources = query_bundle(url, "Patient", query=query)

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
                print(f"Flag/{flag['id']}: \n\n{json.dumps(flag, indent=4)}\n\n")

            # Ask which one(s) to delete
            yes_no(f"Remember which ones to delete! Ready to continue?", default=True)
            flag_ids = []
            while not flag_ids:
                flag_ids = pick(
                    [r["id"] for r in flags],
                    "Select which Flag resources to delete ([space] to select multiple, [enter] to submit):",
                    multi_select=True
                    )

                # Do not allow deleting them all
                if len(flags) == len(flag_ids):
                    print(f"Error: You cannot delete all resources!")
                    flag_ids = []

            # Delete the others
            for flag_id in flag_ids:
                try:
                    # Make the request
                    delete_url = furl(url)
                    delete_url.path.segments.extend(["Flag", flag_id[0]])
                    if not yes_no(f"Are you sure you want to DELETE -> {delete_url.url}?", default=False):
                        continue
                    response = requests.delete(delete_url.url)
                    content = response.content
                    response.raise_for_status()

                    # Print it out
                    print(f"Deleted Flag/{flag_id[0]} successfully")

                except Exception as e:
                    print(f"Error deleting Flag/{flag_id[0]}: {e}")
                    print(f"FHIR response: {content}")

    except Exception as e:
        print(f"Error: {e}")
