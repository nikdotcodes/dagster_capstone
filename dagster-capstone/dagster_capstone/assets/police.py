import requests

from dagster import asset
from . import constants

@asset(
    group_name="raw_files"
)
def police_file():
    """
    The raw zip files from Data.Police.UK
    """

    raw_police_zip = requests.get(
        "https://data.police.uk/data/archive/latest.zip"
    )
    
    with open(constants.POLICE_DATA_ZIP_PATH, 'wb') as output_file:
        output_file.write(raw_police_zip.content)