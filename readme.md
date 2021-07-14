## Generating Sheet-Level Metadata for Map Sets

1. In Argo, find all records to be updated. This can usually be done by searching for the catKey. If using a custom list if DRUIDs, skip to the next step. Under ‘Bulk Actions’, download the descriptive metadata for the objects to be modified. Unzip the folder.

2. Download/copy _addMetadata.py_ and _compile_wrap_descMD.rb_ into the newly created metadata folder.

3. Open a terminal and navigate to the metadata folder.

4. From THIS WORKBOOOK, create a CSV file from the sheet containing the metadata. Update the numbers in the ‘date/sequence designation’ column with leading zeros to ensure that they will list in the proper sequence. Save the file as ‘maps.csv’ in the metadata folder.

5. Run the Python script:

    $ python addMetadata.py

6. Examine a few records to make sure they have updated correctly.

7. Run the Ruby script:

    $ ruby compile_wrap_descMD.rb . metadata.xml
    
8. In Argo, open the objects for versioning. Locate the APO for the map set. Select ‘MODS Bulk Loads” and choose ‘Submit new file.’ Then upload metadata.xml.
