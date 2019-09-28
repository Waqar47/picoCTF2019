#/bin/bash
for i in {1..200};do ./vuln $(python -c "print 'A' * $i"); done

#132 i breaker
