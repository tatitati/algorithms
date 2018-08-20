<?php

function bubleSort(&$list) {
    $total = count($list);

    $i = 1;
    while($i < $total/2-1) {
        swapIteration($list);
        $i++;
    }
}

function swapIteration(&$list)
{
    $total = count($list);

    for($i = 1; $i < $total; $i++) {
        swapIfWrongOrder($list, $i-1, $i);
    }
}

function swapIfWrongOrder(&$list, $i, $j)
{
    if ($list[$i] >= $list[$j]) {
        $a = $list[$i];
        $b = $list[$j];

        $list[$i] = $b;
        $list[$j] = $a;
    }
}

/**
 * @test swapIfWrongOrder
 */
$listA = [1, 10, 9, 5];
swapIfWrongOrder($listA, 1, 3);
assert($listA == [1, 5, 9, 10]);


/**
 * @test swapIteration
 */
$listB = [12, 8, 7, 3];
swapIteration($listB);
assert($listB == [8, 7, 3, 12]);

/**
 * @test bubleSort
 */
$listC = [100, 23, 84, 10, 1, 13, 15, 8, 80, 44, 22, 23, 45, 66, 200, 110];
bubleSort($listC);
assert($listC == [1, 8, 10, 13, 15, 22, 23, 23, 44, 45, 66, 80, 84, 100, 110, 200]);