# Filtering run results

## Total number of records
```
type  count(keywordId)
DS           119326354
GP           145318934
CD            52029226
```

## Total number of distinct label to keyword mappings
```
type  size(collect_set(struct(label, keywordId)))
DS                                         147497
GP                                         546131
CD                                          55922
```

## Total number of distinct label to keyword mappings [after filtering]
```
type  size(collect_set(struct(label, keywordId)))
DS                                         137718
GP                                         456926
CD                                          51687
```
