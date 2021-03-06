<!-- dx-header -->
# Samtools trio calling (DNAnexus Platform App)

Trio calling (with recognition of mendelian violations) using samtools from https://github.com/samtools/samtools/archive/0.1.19.tar.gz

This is the source code for an app that runs on the DNAnexus Platform.
For more information about how to run or modify it, see
https://wiki.dnanexus.com/.
<!-- /dx-header -->

## Caveat:

This applet does not properly handle non-pseudoautosomal regions of the X chromosome correctly.

## getting/building the source

The git repo needs to be checked out with ```git clone --recursive``` to get the samtools source.

If you did not do this and already have the source, try ```git submodule init``` then ```git submodule update```

To build, you need the DNANexus SDK installed, then issue ```dx build``` from within this directory.

## Inputs

* **Input BAM file for child** ``childbam``: ``file``
* **Input BAM file for the father** ``fatherbam``: ``file``
* **Input BAM file for the mother** ``motherbam``: ``file``
>  The input BAM files need to have an appropriate SAMPLE_NAME property which will be used in the output VCF
* **Reference genome** ``reference``: ``file``
* **File containing target regions (.bed)** ``targetbed``: ``file`` (optional)

## Outputs

* **Joint calls with trio MV calculations** ``vcfout``: ``file``
