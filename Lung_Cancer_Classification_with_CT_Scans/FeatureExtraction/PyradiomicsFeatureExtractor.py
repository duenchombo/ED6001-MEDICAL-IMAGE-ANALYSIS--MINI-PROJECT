
# import os

# def extractPyradiomicsFeatures(Lidc_IdrFilesPath:str=None,
#                                pyradiomicsDcmScriptPath:str=None,
#                                pyradiomicsParamsFilePath:str=None,
#                                pyradiomicsFeatureDictFilePath:str=None,
#                                startPatient:int=None,
#                                outputDirectoryPath:str=None,
#                                tempDirectoryPath:str=None) -> None:
    
#     """
#     # Description
#         -> This script iterates through all the patient's folders extracting important data from the .dcm files into a pyradiomics_features.csv file
#     ------------------------------------------------------------------------------------------------------------------------------------------------
#     := param: Lidc_IdrFilesPath - Global path for files from the LIDC-IDR dataset.
#     := param: pyradiomicsDcmScriptPath - Path to the pyradiomics-dcm.py script used to extract features from the images on the dataset [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/tree/master/labs/pyradiomics-dcm].
#     := param: pyradiomicsParamsFilePath - Path for the parameters file with the Pyradiomics feature extractor positional arguments [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/tree/master/labs/pyradiomics-dcm].
#     := param: pyradiomicsFeatureDictFilePath - Path for the features to be considered during the extraction [Available on the pyradiomics GitHub Repository: https://github.com/AIM-Harvard/pyradiomics/blob/master/labs/pyradiomics-dcm/resources/featuresDict_IBSIv7.tsv].
#     := param: startPatient - Number of the Patient to start the extraction from [Allows a better feature extraction management].
#     := param: outputDirectoryPath - Path to the directory for saving the resulting DICOM file.
#     := param: tempDirectoryPath - Path to the directory to store intermediate results [Including the pyradiomic_features.csv].
#     := return: None, since we are simply extracting data from the LIDC-IDR dataset images.
#     """

#     # Add Restrictions to the Script Execution
#     if Lidc_IdrFilesPath is None:
#         raise ValueError('A path for the LIDC-IDR dataset was not given!')
    
#     if pyradiomicsDcmScriptPath is None:
#         raise ValueError('A path for the pyradiomics-dcm.py script was not given!')
    
#     if pyradiomicsParamsFilePath is None:
#         raise ValueError('A path for the Pyradiomics_Params.yaml file was not given!')
    
#     if pyradiomicsFeatureDictFilePath is None:
#         raise ValueError('A path for the featuresDict.tsv file was not given!')
    
#     if outputDirectoryPath is None:
#         raise ValueError('A Output Directory [used to save the resulting DICOM file] was not given!')
    
#     if tempDirectoryPath is None:
#         raise ValueError('A Path to the directory used to store intermediate results was not given!')

#     if not os.path.isabs(Lidc_IdrFilesPath):
#         raise ValueError('The path for the LIDC-IDR dataset is relative! Make sure to use a global path')

#     # Save the Initial working directory
#     initialDirectoryPath = os.getcwd()

#     # Setting default parameters
#     startPatient = 0 if startPatient is not None else startPatient
#     startPatient = 0 if startPatient is not None else startPatient

#     # Switch to the path with the LIDC-IDR dataset
#     os.chdir(Lidc_IdrFilesPath)
#     main_directory = os.listdir()

#     # Iterate through all the Patients
#     for patient in main_directory:
#         # Skip the output and temp directories alonsgside all the unnecessary patient files (according to the initial patient) and other non-directory files
#         if (not os.path.isdir(patient)) or patient == "OutputSR" or patient == "TempDir" or startPatient > int(patient[len(patient)-4:]):
#             continue
        
#         # Get the current Patient's Data Folder (Contains the CT-Scan and X-Ray)
#         patientFolders = os.listdir(patient)
#         path = ""
#         content = 0
        
#         # Finding the CT-scan folder (has the most content - directories with each segmentation and directory with the input DICOM series)
#         for folder in patientFolders:
#             segmentations_or_series = os.listdir(patient + "\\" + folder)
#             if (len(segmentations_or_series) > content):
#                 content = len(segmentations_or_series)
#                 path = folder
        
#         # Save the Directory with the Patient's Scans
#         patientScansFolder = os.listdir(patient + "\\" + path)
#         main = ""

#         # Finding the series folder
#         for folder in patientScansFolder:
#             if not "Annotation" in folder:
#                 main = folder
#                 break
        
#         # Create a index to track the current segmentation
#         seg_index = 1
        
#         # Iterate through all the segmentations and extract their features into a new entry on the .csv output file [Identified with <Patient_Name>-<Segmentation_Number> nomenclature]
#         for folder in patientScansFolder:
#             if "Segmentation" in folder:
#                 # print("\n\nPACIENT [" + patient + "] - SEGMENTATION [" + str(seg_index) + "]")
#                 os.system(f'"""python {pyradiomicsDcmScriptPath} --input-image-dir "{patient}\{path}\{main}" --input-seg-file "{patient}\{path}\{folder}\\1-1.dcm" --output-dir {outputDirectoryPath} --temp-dir {tempDirectoryPath} --parameters {pyradiomicsParamsFilePath} --features-dict {pyradiomicsFeatureDictFilePath} --name {patient}-{seg_index}"""')
#                 seg_index+=1
    
#     # Go back to the initial directory
#     os.chdir(initialDirectoryPath)




import os
import sys

def extractPyradiomicsFeatures(Lidc_IdrFilesPath: str = None,
                               pyradiomicsDcmScriptPath: str = None,
                               pyradiomicsParamsFilePath: str = None,
                               pyradiomicsFeatureDictFilePath: str = None,
                               startPatient: int = 0,
                               outputDirectoryPath: str = None,
                               tempDirectoryPath: str = None) -> None:
    """
    Extract Pyradiomics features from LIDC-IDR DICOM dataset.

    Parameters
    ----------
    Lidc_IdrFilesPath : str
        Path to the root folder of the LIDC-IDR dataset.
    pyradiomicsDcmScriptPath : str
        Path to the 'pyradiomics-dcm.py' script.
    pyradiomicsParamsFilePath : str
        Path to the 'Pyradiomics_Params.yaml' file.
    pyradiomicsFeatureDictFilePath : str
        Path to the 'featuresDict.tsv' file.
    startPatient : int
        Patient number to start extraction from.
    outputDirectoryPath : str
        Directory to save the resulting DICOM output.
    tempDirectoryPath : str
        Directory to store intermediate results.
    """

    # --- Validation checks ---
    if not Lidc_IdrFilesPath:
        raise ValueError("❌ LIDC-IDR dataset path is required.")
    if not pyradiomicsDcmScriptPath:
        raise ValueError("❌ Path to pyradiomics-dcm.py script is required.")
    if not pyradiomicsParamsFilePath:
        raise ValueError("❌ Path to Pyradiomics_Params.yaml file is required.")
    if not pyradiomicsFeatureDictFilePath:
        raise ValueError("❌ Path to featuresDict.tsv file is required.")
    if not outputDirectoryPath:
        raise ValueError("❌ Output directory path is required.")
    if not tempDirectoryPath:
        raise ValueError("❌ Temporary directory path is required.")

    # --- Save original working directory ---
    initialDirectoryPath = os.getcwd()

    try:
        # ✅ Convert to absolute paths before changing directory
        pyradiomicsDcmScriptPath = os.path.abspath(pyradiomicsDcmScriptPath)
        pyradiomicsParamsFilePath = os.path.abspath(pyradiomicsParamsFilePath)
        pyradiomicsFeatureDictFilePath = os.path.abspath(pyradiomicsFeatureDictFilePath)
        outputDirectoryPath = os.path.abspath(outputDirectoryPath)
        tempDirectoryPath = os.path.abspath(tempDirectoryPath)

        # Change to LIDC dataset directory
        os.chdir(Lidc_IdrFilesPath)

        # Iterate through all patient folders
        for patient in os.listdir():
            if (not os.path.isdir(patient)) or patient in ["OutputSR", "TempDir"]:
                continue

            try:
                patient_num = int(patient[-4:])
                if startPatient > patient_num:
                    continue
            except ValueError:
                continue  # skip non-numeric patient folders

            # Find the CT-scan folder (most content)
            patientFolders = os.listdir(patient)
            path = max(patientFolders, key=lambda f: len(os.listdir(os.path.join(patient, f))))

            patientScansFolder = os.listdir(os.path.join(patient, path))
            main = next((f for f in patientScansFolder if "Annotation" not in f), None)

            seg_index = 1
            for folder in patientScansFolder:
                if "Segmentation" in folder:
                    input_image_dir = os.path.join(patient, path, main)
                    input_seg_file = os.path.join(patient, path, folder, "1-1.dcm")

                    cmd = (
                        f'python "{pyradiomicsDcmScriptPath}" '
                        f'--input-image-dir "{input_image_dir}" '
                        f'--input-seg-file "{input_seg_file}" '
                        f'--output-dir "{outputDirectoryPath}" '
                        f'--temp-dir "{tempDirectoryPath}" '
                        f'--parameters "{pyradiomicsParamsFilePath}" '
                        f'--features-dict "{pyradiomicsFeatureDictFilePath}" '
                        f'--name "{patient}-{seg_index}"'
                    )

                    # print(f"⚙️ Extracting features for {patient} - Segmentation {seg_index}")
                    os.system(cmd)
                    seg_index += 1

    except Exception as e:
        print(f"❌ Error during extraction: {e}", file=sys.stderr)

    finally:
        # ✅ Always return to original working directory
        os.chdir(initialDirectoryPath)
        print(f"✅ Working directory restored to: {initialDirectoryPath}")
