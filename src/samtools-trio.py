#!/usr/bin/env python
# samtools-trio 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See https://wiki.dnanexus.com/Developer-Portal for documentation and
# tutorials on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

import os
import dxpy
import subprocess
from subprocess import check_call as scc
from subprocess import check_output as sco

@dxpy.entry_point('main')
def main(inputbams, reference, outputbase, targetbed=None):

    inputbams = [dxpy.DXFile(item) for item in inputbams]

    if len(inputbams) != 3:
        raise dxpy.exceptions.AppError("A trio must consist of three files (%d bam files were provided)"%len(inputbams))

    scc("dx download '%s' -o - --no-progress | zcat > reference.fa"%dxpy.DXFile(reference).get_id(), shell=True)
    scc(["samtools", "faidx", "reference.fa"])

    targetopt = ''
    if not targetbed is None:
        dxpy.download_dxfile(targetbed, "target.bed")
        targetopt = '-l target.bed'

    # order in trioconfig must be child, father, mother
    trioconfig = open('trioconfig', 'w')
    inputfiles = []
    for i in range(len(inputbams)):
        dxpy.download_dxfile(inputbams[i].get_id(), "inputbams-%d.bam"%i)
        inputfiles.append("inputbams-%d.bam"%i)
        trioconfig.write(str(inputbams[i].get_properties()['SAMPLE_NAME']) + "\n")

    trioconfig.close()

    # could tee to an output bcf file if desired
    # FIXME - need to specify child's gender for non-PAR on X
    #        trioxd for female child, trioxs for male child
    command = """samtools mpileup -uf reference.fa -D -V -C 50 %s %s | \
        bcftools view -s trioconfig -T trioauto -vg - > %s.vcf \
    """%(targetopt, ' '.join(inputfiles), outputbase)

    print "::: command is:\n\t" + command
    scc(command, shell=True)

    #bcfout = dxpy.upload_local_file("bcfout");
    vcfout = dxpy.upload_local_file("%s.vcf"%outputbase);

    output = {}
    #output["bcfout"] = dxpy.dxlink(bcfout)
    output["vcfout"] = dxpy.dxlink(vcfout)

    return output

dxpy.run()