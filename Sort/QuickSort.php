<?php

function quickSort($list) {
    if (count($list) < 2) {
        return $list;
    } else {
        $pivotIndex = array_rand($list, 1);
        $lowers = extractLowersThanPivot($list, $pivotIndex);
        $biggers = extractBiggersThanPivot($list, $pivotIndex);

        return joinArrays(
            quickSort($lowers),
            $list[$pivotIndex],
            quickSort($biggers)
        );
    }
}

function joinArrays($listA, $pivot, $listB)
{
    return array_merge($listA, [$pivot], $listB);
}

function extractLowersThanPivot($list, $i)
{
    $lowers = [];
    foreach ($list as $j => $item) {
        if ($i == $j) {
            // is the pivot
            continue;
        }

        if ($item <= $list[$i]) {
            $lowers[] = $item;
        }
    }

    return $lowers;
}

function extractBiggersThanPivot($list, $i)
{
    $biggers = [];
    foreach ($list as $j => $item) {
        if ($i == $j) {
            // is the pivot
            continue;
        }

        if ($list[$i] < $item) {
            $biggers[] = $item;
        }
    }

    return $biggers;
}

/**
 * @test joinArrays
 */
$list1 = [1, 11, 111];
$pivot = 2;
$list3 = [3, 33, 333];
assert(joinArrays($list1, $pivot, $list3) == [1, 11, 111, 2, 3, 33, 333]);

/**
 * @test extractLowersThanPivot
 */
$lowers = extractLowersThanPivot([10, 1, 5, 2, 7, 15], 4);
assert($lowers == [1, 5, 2]);

/**
 * @test extractBiggersThanPivot
 */
$lowers = extractBiggersThanPivot([18, 15, 1, 5, 7, 10], 4);
assert($lowers == [18, 15, 10]);

/**
 * @test extractBiggersThanPivot
 */
$result = quickSort([18, 15, 1, 5, 7, 10], 4);
assert($result == [1, 5, 7, 10, 15, 18]);