<!-- dx-header -->
# Samtools trio calling (DNAnexus Platform App)

Trio calling (with recognition of mendelian violations) using samtools from https://github.com/samtools/samtools/archive/0.1.19.tar.gz

This is the source code for an app that runs on the DNAnexus Platform.
For more information about how to run or modify it, see
https://wiki.dnanexus.com/.
<!-- /dx-header -->

## Caveat:

This applet does not properly handle non-pseudoautosomal regions of the X chromosome correctly.

## Inputs

* **Input BAM files (in order child, father, mother)** ``inputbams``: ``array:file``
>  It is important that the input BAM files be provided in this order (since the
>  order is used to create the ``trioconfig`` file)
* **Reference genome** ``reference``: ``file``
* **File containing target regions (.bed)** ``targetbed``: ``file`` (optional)

## Outputs

* **Joint calls with trio MV calculations** ``vcfout``: ``file``