#!/usr/bin/env python3
import sys
import json
import argparse
from datetime import datetime

def extract_info(vcf_file):
    data = []
    biosample_id = None

    with open(vcf_file, 'r') as f:
        for line in f:
            if line.startswith('#CHROM'):
                biosample_id = line.strip().split('\t')[-1]
            elif not line.startswith('#'):
                columns = line.strip().split('\t')
                chrom = columns[0]
                pos = int(columns[1])
                ID = columns[2]
                info = dict(item.split('=') for item in columns[7].split(';'))

                variantType = columns[4]  # Set a default value for variantType
                if "<DEL>" in variantType:
                # If "<DEL>" is found, replace it with "DEL" and remove the "<>"
                    variantType = variantType.replace("<DEL>", "DEL")
                elif "<DUP>" in variantType:
                    variantType = variantType.replace("<DUP>", "DUP")

                variant_id = None
                cn_count = float(columns[9].split(':')[2])
                cn_value = float(columns[9].split(':')[1])
                if cn_count == 1:
                    variant_id = "EFO:0030068"
                    variantState= "low-level loss"
                elif cn_count == 0:
                    variant_id = "EFO:0030069"
                    variantState= "complete genomic loss"
                elif 2 < cn_count < 4:
                    variant_id = "EFO:0030071"
                    variantState= "low-level gain"
                elif cn_count > 4:
                    variant_id = "EFO:0030072"
                    variantState= "high-level gain"
                else:
                    if variantType == "DEL":
                        variant_id = "EFO:0030067"
                        variantState= "copy number loss"
                    elif variantType == "DUP":
                        variant_id = "EFO:0030070"
                        variantState= "copy number gain"

                variant_internal_id = f"{chrom}:{pos}-{info['END']}:{variant_id}"

                data.append({
                    "biosampleId": biosample_id,
                    "assemblyId": "GRCh38",
                    "variantInternalId": variant_internal_id,
                    "variantState": {
                        "id": variant_id,
                        "label": variantState
                    },
                    "definitions": {
                        "Location": {
                            "start": pos,
                            "end": int(info['END']),
                            "chromosome": chrom.split('chr')[1],
                        }
                    },
                    "info": {
                        "legacyId": ID,
                        "cnCount": int(cn_count),
                        "cnValue": cn_value
                    },
                    "updated": datetime.now().isoformat()
                })


    return data

def cnv_vcf2json(args=None):
    parser = argparse.ArgumentParser(description="Convert VCF to JSON")
    parser.add_argument("-i", "--input", type=str, default="", dest="input", help="Input VCF file name")
    parser.add_argument("-o", "--output", type=str, default="", dest="output", help="Output JSON file name")
    args = parser.parse_args(args)

    if not args.input or not args.output:
        parser.print_help()
        sys.exit(1)
    
    input_vcf = args.input
    output_json = args.output

    data = extract_info(input_vcf)

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    cnv_vcf2json(sys.argv[1:])
