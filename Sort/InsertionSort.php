<?php

function insertionSort($a)
{
    $total = count($a);

    // forward loop
    for ($f=1; $f<=$total-1; $f++) {
        if ($a[$f-1] > $a[$f]) {
            // backward loop
            swapItemsBackwardFrom($a, $f);
        }
    }

    print_r($a);
}



function swapItemsBackwardFrom(&$list, $f)
{
    $num = $list[$f];

    for($b = $f-1; $b >= 0; $b--) {
        if ($list[$b] >= $num) {
            // then our number must be before (we swap)
            $list[$b+1] = $list[$b];
            $list[$b] = $num;
        }
    }
}

insertionSort([23, 84, 10, 1, 13, 8, 80, 44, 22, 23, 45, 66]);
// Result: [1, 8, 10, 13, 22, 23, 23, 44, 45, 66, 80, 84]