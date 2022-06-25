# trello-me
A personal trello api python wrapper for daily job which can not be done by offical website and app. 

## Query list in board

```
poetry run filter-list -k trello_key -t trello_token -n regex_filter board_name_regex
```

## Query card in board

```
poetry run filter-card -k trello_key -t trello_token -n regex_filter board_name_regex
```
