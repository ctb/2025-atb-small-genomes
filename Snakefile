SUFFIXES, = glob_wildcards('run-paths.txt.{suffix}')

rule all:
    input:
        expand("sublineages.x.run-paths.txt.{s}", s=SUFFIXES)

rule manysearch:
    input:
        query = "sublineages.sig.zip",
        paths = "run-paths.txt.{suffix}"
    output:
        csv = "sublineages.x.run-paths.txt.{suffix}",
        log = "sublineages.x.run-paths.log.{suffix}",
    threads: 20
    shell: """
       /usr/bin/time -v sourmash scripts manysearch -k 21 -t .01 -s 1000 \
            {input.query} {input.paths} \
            -o {output.csv} -c {threads} >& {output.log} 
    """
