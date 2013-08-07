# samtools-trio Developer Readme

samtools is used to index the input bam files as they are being loaded (using ``tee`` and a pipe), so .bai files do not need to be provided.

## Handling the allosomes

The sex chromosomes are an edge case for trio calling. But you cannot just
consider the X and Y chromosomes as a whole, you need to consider the
pseudoautosomal regions (PARs). These can be determined from the Ensembl
database with:

```
select (select sr.name from seq_region sr
         where sr.seq_region_id=ae.seq_region_id) as chrom_1,
       ae.seq_region_start as start_1, ae.seq_region_end as end_1,
       (select sr.name from seq_region sr
         where sr.seq_region_id=ae.exc_seq_region_id) as chrom_2,
       ae.exc_seq_region_start as start_2, ae.exc_seq_region_end as end_2
  from assembly_exception ae where ae.exc_type="PAR";
```

so, for hg19:

Y:10001-2649520 is homologous to X:60001-2699520
and
Y:59034050-59373566 is homologous to X:154931044-155270560


## Running this app with additional computational resources

This app has the following entry points:

* main

When running this app, you can override the instance type to be used by
providing the ``systemRequirements`` field to ```/applet-XXXX/run``` or
```/app-XXXX/run```, as follows:

    {
      systemRequirements: {
        "main": {"instanceType": "dx_m1.large"}
      },
      [...]
    }

See <a
href="https://wiki.dnanexus.com/API-Specification-v1.0.0/IO-and-Run-Specifications#Run-Specification">Run
Specification</a> in the API documentation for more information about the
available instance types.

