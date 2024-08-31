## Create a databasis 
### Create a txt file with pathnames. 
### Create an output folder 
### Create a directory parser which takes this txt file and collect all files with given extensions (pdf,docx)
### Create a file worker which collects the data from the found files
#### With all files
1. Extract Metadata
#### With pdf files
1. Extract Text
2. Count Images
3. Decide if Images are necessary to understand the content of the file
4. If necessary: Convert the pages to images.
5. Create a json file with all information and link to Images
#### With docx files
1. Converte to pdf
2. Alternative: Extract text

## Submit data to ChatGPT
### Give ChatGPT the order to analyze the given information and respond with summary, label, categories
