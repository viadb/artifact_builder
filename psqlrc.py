import json
from filemap import fileMap
from re import sub
"""
generatePsqlrc generates a psqlrc file
"""
def generatePsqlrc(dataMap: fileMap, psqlrc_output: str) -> any:
    header = ("""
\set QUIET ON
\set QUIET OFF
\echo '\\nCurrent Host Server Date Time : '`date` '\\n'
\echo '\\n\\t:menu -- Help Menu\t:sp-- Current Search Path\\t:clear -- Clear screen\\t:ll -- List\\n'
\set menu '\\\i ~/.psqlrc'\\n
    """)

    with open(psqlrc_output, 'w+', encoding='utf-8-sig') as f:
        f.write(header)
        for item in dataMap.values():
            """
            We remove comments on the query and then, we encode for 
            escaping new lines in the query.
            split('--',1)[0] is not very efficient here
            """
            onelinerQuery=str(item['query']).encode('unicode_escape').decode("utf-8")

            """
            Titles should not have any special characters nor neither spaces
            """
            sanitizeTitle=sub(r"[\s]|[-_]","",str(item['title']))
            line=f"\n\set {sanitizeTitle} \'{onelinerQuery}\'\n"
            f.write(line)
    
