<?php

function insertionSort(&$a)
{
    $total = count($a);

    // forward loop
    for ($i=1; $i<=$total-1; $i++) {
        if ($a[$i-1] > $a[$i]) {
            // backward loop to swap numbers if necessay until put it in the right place
            putItemInRightPlace($a, $i);
        }
    }
}

function putItemInRightPlace(&$list, $j)
{
    for($b = $j-1; $b >= 0; $b--) {
        swapIfWrongOrder($list, $b, $b+1);
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
 * @test putItemsInRightPosition
 */
$listB = [5, 8, 9, 6];
putItemInRightPlace($listB, 3);
assert($listB == [5, 6, 8, 9]);

/**
 * @test insertionSort
 */
$listC = [23, 84, 10, 1, 13, 15, 8, 80, 44, 22, 23, 45, 66];
insertionSort($listC);
assert($listC == [1, 8, 10, 13, 15, 22, 23, 23, 44, 45, 66, 80, 84]);