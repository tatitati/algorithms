<?php

function insertionSort(&$a)
{
    $total = count($a);

    // forward loop
    for ($f=1; $f<=$total-1; $f++) {
        if ($a[$f-1] > $a[$f]) {
            // backward loop
            putItemInRightPlace($a, $f);
        }
    }
}

function putItemInRightPlace(&$list, $f)
{
    $num = $list[$f];

    for($b = $f-1; $b >= 0; $b--) {
        if ($list[$b] >= $num) {
            swap($list, $b+1, $b);
        }
    }
}

function swap(&$list, $i, $j)
{
    $a = $list[$i];
    $b = $list[$j];

    $list[$i] = $b;
    $list[$j] = $a;
}

/**
 * @test SWAP
 */
$listA = [8, 9, 3];
swap($listA, 0, 2);
assert($listA == [3, 9, 8]);

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