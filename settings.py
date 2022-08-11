"""
    Module for configuring the script
"""

import os


def get_full_file_path(path, filename):
    """Combines path and filename to return full abs path as raw string"""
    return (
        os.path.abspath(os.path.join(path, filename)).encode("unicode-escape").decode()
    )


def get_full_path(path):
    """Combines path and filename to return full abs path as raw string"""
    return os.path.abspath(path).encode("unicode-escape").decode()


##############################################
############### INPUT RELATED ################
##############################################

# _ is used as a delimeter to split the filename of the pdf
# This index is for which item in the list (from split) corresponds to the
# ID of an applicant
pdf_filename_split_delimeter = "_"
pdf_filename_split_index = 2

path_to_pdfs_to_extract = os.path.join(".", "testing", "case_3", "pdfs")
path_to_pdfs_to_extract = get_full_path(path_to_pdfs_to_extract)

qualification_mapping_filename = "mapping.xlsx"
qualification_mapping_sheet_name = "Mapping"
path_to_mapping_file = os.path.join(".", "testing", "case_3", 'pdfs')
path_to_mapping_file = get_full_file_path(
    path_to_mapping_file, qualification_mapping_filename
)

# target_ucas_id_file = "target_ids.xlsx"
target_ucas_id_file = "Batch 1.xlsx"
is_id_file_banner = True
is_banner_cumulative = True
which_column = "F"
# is_id_file_banner = False
# is_banner_cumulative = False
# which_column = None

path_to_target_file = path_to_pdfs_to_extract
path_to_target_file = get_full_file_path(path_to_target_file, target_ucas_id_file)

database_headers = ["ID No.", "Batch No.", "Timestamp"]
database_header_id_num_index = 0
database_header_batch_index = 1
database_header_timestamp_index = 2

assert (
    max(
        database_header_id_num_index,
        database_header_batch_index,
        database_header_timestamp_index,
    )
    < len(database_headers)
)

database_of_extracted_pdfs = "previously_extracted.csv"
path_to_database_of_extracted_pdfs = get_full_file_path(
    os.path.join(".", "testing", "case_3", "data"), database_of_extracted_pdfs
)

terminate_if_batch_num_repeated = True

# IMPORTANT NOTE: IT IS ASSUMED THAT THE BATCH NUMBERS WILL KEEP INCREASING
# EVEN AFTER THE CYCLE CHANGES! THIS IS VITAL FOR THE REMAINING WORKFLOW!
# THE BATCH NUMBERS MUST BE UNIQUE!!!
batch_number = 1
cycle = "Nov"
allocation_details = {
    "AP": 1,
    "TM": 1,
    "EN": 1,
}

##############################################
############### OUTPUT RELATED ###############
##############################################

path_to_pdf_pool = os.path.join(".", "testing", "case_3", "output", "pool")
path_to_pdf_pool = get_full_path(path_to_pdf_pool)

output_path = os.path.join(".", "testing", "case_3", "output")
output_path = get_full_path(output_path)

output_filename = f"grades_{batch_number}.xlsx"

log_filename = f"execution_log_{batch_number}.log"
path_to_log = get_full_file_path(output_path, log_filename)
ids_in_folder_file = f"id_log_{batch_number}.txt"
path_to_folder_ids = get_full_file_path(output_path, ids_in_folder_file)
