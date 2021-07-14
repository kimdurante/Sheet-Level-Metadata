## Generating Sheet-Level Metadata for Map Sets

1. In Argo, find all records to be updated. This can usually be done by searching for the catKey. If using a custom list if DRUIDs, skip to the next step. 

2. Under ‘Bulk Actions’, download the descriptive metadata for the objects to be modified. Unzip the folder.

3. Download/copy _addMetadata.py_ and _compile_wrap_descMD.rb_ into the newly created metadata folder.

4. Open a terminal and navigate to the metadata folder.

5. From [this workbook](https://docs.google.com/spreadsheets/d/1IhJo47bqmKCL4EclgMLTOfBJWyxP-TOwtkHs8Xz-pX4/edit?ts=6001d879#gid=0), create a CSV file from the sheet containing the metadata. Update the numbers in the ‘date/sequence designation’ column with leading zeros to ensure that they will list in the proper sequence. Save the file as ‘_maps.csv_’ in the metadata folder.

6. Run the Python script:

    $ python addMetadata.py

7. Examine a few records to make sure they have updated correctly.

8. Run the Ruby script:

    $ ruby compile_wrap_descMD.rb . metadata.xml
    
9. In Argo, open the map objects for versioning. 

10. Locate the APO for the map set. Select ‘MODS Bulk Loads” and choose ‘Submit new file.’ 

    Select the file (_metadata.xml_) and choose 'MODS XML input; load into objects.'
    
11. Close object versions.
