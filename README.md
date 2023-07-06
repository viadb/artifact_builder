# Artifact Builder

This section builds a JSON map of the SQL and MD files present on the repository, and structure them in the form of a Opensearh-compatible schema for later import into a searcher endpoint.

## Execution

Load virtual env:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

The folowing allows you to index and search:

```bash
python3 artifact_builder/ -D sql -E postgresql -v | jq '.search_query'
```

See `python3 artifact_builder/ -h` for more information.

Default output: index.json (with `--output`) and `--ouput-ndjson` (`ndindex.json`).

## Development

This repository serves the builder for several repositories. You can test/work on 
your foreign repository as a submodule. 

This repository has no tags, so for testing, you'll need to create a branch and use
that branch in your foreign repository, in a branch. 

Steps:

eg: you're coding pgqueries, and need to test artifact_builder:

- You create a branch in pgqueries,
- You enter artifact_builder and do your work, commit that work in a new branch (for artifact_builder)
- Push artifact_builder changes remotely
- Push changes of pgqueries (in this case, it'll update just the commit pointing to artifact_builder)
- Use beta or alpha tags in pgqueries so it builds the development artifacts.

## TODO 

Modules [potentially] beneficial: [Dataclasses](https://github.com/lidatong/dataclasses-json)
