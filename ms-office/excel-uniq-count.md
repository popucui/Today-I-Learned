## Problem

Count the uniq items in a column

## Solution
use the formula below:
`=SUMPRODUCT(1/COUNTIF(B3:B221,B3:B221))`

Explain the meaning:
> 
- 1/: require the items be unique
- COUNTIF: function to perform counting.
    + 1st parameter: range to look for
    + 2nd parameter: creteria required

Refer to [this post from ms](https://support.office.com/en-us/article/COUNTIF-function-E0DE10C6-F885-4E71-ABB4-1F464816DF34) for detail.

