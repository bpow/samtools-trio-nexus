SAMTOOLS_SRC:=samtools

all: samtools bcftools

dirs:
	mkdir -p resources/usr/local/bin

samtools: dirs
	make -C $(SAMTOOLS_SRC)
	cp $(SAMTOOLS_SRC)/samtools resources/usr/local/bin/

bcftools: dirs
	make -C $(SAMTOOLS_SRC)/bcftools
	cp $(SAMTOOLS_SRC)/bcftools/bcftools resources/usr/local/bin/

clean:
	rm -rf resources/usr/local/bin

.PHONY: all dirs samtools bcftools
