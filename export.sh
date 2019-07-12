#!/usr/bin/env bash

@error

set -ex

cd "$( dirname "${BASH_SOURCE[0]}" )"

./mysql2csv -q "SELECT * FROM vw_details_report;" -n details || echo 'Error generating Details Report' >&2
./mysql2csv -q "CALL sp_summary(NULL);" -n summary || echo 'Error generating Summary Report' >&2
./mysql2csv -q "CALL sp_university(NULL);" -n university || echo 'Error generating University Report' >&2

echo 'Finish!'
