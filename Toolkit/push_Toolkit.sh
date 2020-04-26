#!/bin/bash

git status
git pull
echo "你有大概8秒时间确认/You have about 8s to have a check"
for i in {1..2};
do
    ping 192.0.2.2 -n 1 > nul;
done

git add Toolkit
git commit -m "Part 1: This is a small change by master."
git push origin master
git status

echo "1分钟，再检查一下/1m, check again"
ping 192.0.2.2 -n 1 -w 60000 > nul