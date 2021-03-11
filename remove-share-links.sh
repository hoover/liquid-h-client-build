#!/bin/bash -ex

cd "$(dirname ${BASH_SOURCE[0]})"

for URL in 'https://www.facebook.com' 'mailto:?subject' 'https://plus.google.com' 'https://twitter.com' 'https://hyp.is'; do

  SED_LINE="s|$URL[^\"\\<>\'']*||g"
  echo "$SED_LINE"
  find $1 -type f -exec sed -i $SED_LINE {} \;

done
