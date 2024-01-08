# R Notes

## Data Visualisation

### Scatter Plot

```ggplot```

```R
ggplot(data = myData, aes(x = myX, y = myY)) + geom_point(aes(shape=myGroup, color=myGroup)) + facet_wrap(~myGroup) + labs(title=myTitle)
```


