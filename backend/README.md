# Endpoints

<ul>
<li>Create day</li>
<li>Read day</li>
<li>Update day</li>
<li>Delete day</li>
</ul>

db JSON example:

```
{
"01/01/2000" : {
    "feeling" : 8,
    "meds yesterday" : {
        "name": "Depakine Crono",
        "quantity" : 2
    }
    }
    "02/01/2000" : {
    "feeling" : 4,
    "meds yesterday" : {
        "name" : "Depakine Crono",
        "quantity" : 2,
        "name" : "Olanzapin 0.75 g"
        "quantity" : 1
    }
    }
}
```

The feeling goes from 1 to 10, 1 being excrutiatingly depressed to 10 being manic alert. 8 is elevated, 9 is hypomanic and 10 is full blown mania.
