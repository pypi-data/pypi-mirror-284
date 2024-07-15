# snailz: re-make synthetic data

# check required variables have been defined
USAGE=Usage: make DATA=dir PARAMS=dir target
ifndef DATA
  $(error DATA not defined: ${USAGE})
endif
ifndef PARAMS
  $(error PARAMS not defined: ${USAGE})
endif

# readable labels for build targets
.PHONY: commands datasets survey mangled db plates assays samples genomes grids

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## datasets: make all datasets
datasets: \
  ${DATA}/lab.db \
  ${DATA}/mangled/.touch \
  ${DATA}/designs/.touch \
  ${DATA}/readings/.touch \
  ${DATA}/grids/.touch \
  ${DATA}/survey.png

## survey: generate survey map
survey: ${DATA}/survey.png
${DATA}/survey.png: ${DATA}/samples.csv
	snailz survey \
	--outfile $@ \
	--samples ${DATA}/samples.csv

## mangled: create inconsistent plate files
mangled: ${DATA}/mangled/.touch
${DATA}/mangled/.touch: ${DATA}/lab.db ${DATA}/readings/.touch
	@mkdir -p ${DATA}/mangled
	snailz mangle \
	--dbfile ${DATA}/lab.db \
	--tidy ${DATA}/readings \
	--outdir ${DATA}/mangled
	touch ${DATA}/mangled/.touch

## db: generate database
db: ${DATA}/lab.db
${DATA}/lab.db: ${DATA}/assays.json ${DATA}/samples.csv ${DATA}/genomes.json
	@mkdir -p ${DATA}
	snailz db \
	--dbfile $@ \
	--assays ${DATA}/assays.json \
	--samples ${DATA}/samples.csv \
	--sites ${PARAMS}/sites.csv \
	--surveys ${PARAMS}/surveys.csv

## plates: generate plate files
plates: ${DATA}/designs/.touch ${DATA}/readings/.touch
${DATA}/designs/.touch ${DATA}/readings/.touch: ${PARAMS}/assays.json ${DATA}/assays.json
	@rm -rf ${DATA}/designs ${DATA}/readings
	@mkdir -p ${DATA}/designs ${DATA}/readings
	snailz plates \
	--assays ${DATA}/assays.json \
	--designs ${DATA}/designs \
	--params ${PARAMS}/assays.json \
	--readings ${DATA}/readings
	touch ${DATA}/designs/.touch ${DATA}/readings/.touch

## assays: generate assay files
assays: ${DATA}/assays.json
${DATA}/assays.json: ${PARAMS}/assays.json ${DATA}/genomes.json ${DATA}/samples.csv
	@mkdir -p ${DATA}
	snailz assays \
	--genomes ${DATA}/genomes.json \
	--outfile $@ \
	--params ${PARAMS}/assays.json \
	--samples ${DATA}/samples.csv

## samples: sample snails from survey sites
samples: ${DATA}/samples.csv
${DATA}/samples.csv: ${DATA}/genomes.json ${PARAMS}/samples.json ${PARAMS}/sites.csv ${PARAMS}/surveys.csv ${DATA}/grids/.touch
	@mkdir -p ${DATA}
	snailz samples \
	--genomes ${DATA}/genomes.json \
	--grids ${DATA}/grids \
	--outfile $@ \
	--params ${PARAMS}/samples.json \
	--sites ${PARAMS}/sites.csv \
	--surveys ${PARAMS}/surveys.csv

## genomes: synthesize genomes
genomes: ${DATA}/genomes.json
${DATA}/genomes.json: ${PARAMS}/genomes.json
	@mkdir -p ${DATA}
	snailz genomes \
	--outfile $@ \
	--params ${PARAMS}/genomes.json

## grids: synthesize pollution grids
grids: ${DATA}/grids/.touch
${DATA}/grids/.touch: ${PARAMS}/grids.json ${PARAMS}/sites.csv
	@rm -rf ${DATA}/grids
	@mkdir -p ${DATA}/grids
	snailz grid \
	--grids ${PARAMS}/grids.json \
	--outdir ${DATA}/grids \
	--sites ${PARAMS}/sites.csv
	touch ${DATA}/grids/.touch
