﻿# CPFirebaseCopyPaste

This is for use with Clever Programmer's Diseny+ Clone.

I created it to avoid having to manually put in each of the entires into the database.

## How it works

Included in the directory is the `data.json` file, which contains all of the entires to be added to the database.

This loops through each entry, getting the keys and values, and will type the values into the firebase "Add a Document" screen for you so you don't have to.

## Demo
https://user-images.githubusercontent.com/63256944/232254744-3d059a64-1f8a-4896-a4ff-2bb03ad0983f.mp4

## How to use it.

1. Open your firebase, and go to your Cloud Firestore.
2. First add the `movies` collection.
3. Then press "Add a document"
4. From here, click on Auto ID to generate a random ID, then create 7 empty field.
5. Click on the very first field, so it has focus, and then press Tab.
6. When it's done, press save, then repeat the steps again until all entries are done!

## Extra

That's it, The program will then select the entry, and go through each field, inserting the appropiate data.
