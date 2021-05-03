<?php

function quickSort($list) {
    if (count($list) < 2) {
        return $list;
    }

    $pivotIndex = array_rand($list, 1);
    $lowers = extractLowersThanPivot($list, $pivotIndex);
    $biggers = extractBiggersThanPivot($list, $pivotIndex);

    return joinItems(
        quickSort($lowers),
        $list[$pivotIndex],
        quickSort($biggers)
    );
}

function joinItems($listA, $pivot, $listB)
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