<?php

function selectionSort(&$list)
{
    foreach($list as $i => $n) {
        $minJ = findPositionOfMinimumFromPosition($list, $i);
        swap($list, $i, $minJ);
    }
}

function findPositionOfMinimumFromPosition($list, $j)
{
    $minimum = null;
    $minimumPos = null;
    $totalSubarray = count($list);

    for($i = $j; $i < $totalSubarray; $i++) {
        if ($minimum === null || $list[$i] < $minimum) {
            $minimum = $list[$i];
            $minimumPos = $i;
        }
    }

    return $minimumPos;
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
 * @test findMinimum
 */
$listB = [84, 1, 30, 5, 16];
assert(findPositionOfMinimumFromPosition($listB, 2) == 3); // list[3] = 5
assert(findPositionOfMinimumFromPosition($listB, 0) == 1); // list[1] = 1

/**
 * @test selectionSort
 */
$listC = [23, 84, 10, 1, 13, 15, 8, 80, 44, 22, 23, 45, 66];
selectionSort($listC);
assert($listC == [1, 8, 10, 13, 15, 22, 23, 23, 44, 45, 66, 80, 84]);