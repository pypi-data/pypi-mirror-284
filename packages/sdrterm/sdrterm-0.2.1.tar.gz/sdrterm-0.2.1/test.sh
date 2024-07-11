if [[ -z ${DSD_CMD} ]]; then
  DSD_CMD="dsd -q -i - -o /dev/null -n";
fi

if [[ -z ${OUT_PATH} ]]; then
  OUT_PATH=/tmp;
fi

export DSD_CMD="$DSD_CMD";
export OUT_PATH="$OUT_PATH";

echo "$OUT_PATH";
echo "$DSD_CMD";

declare -A sums;

sums["${OUT_PATH}/outB.wav"]="b8058749ff0e25eab70f92dda86c2507";
sums["${OUT_PATH}/outd.wav"]="d51e36787d2cf8a10be87a1e123bb976";
sums["${OUT_PATH}/outf.wav"]="07e31be2ff4f16b91adcf540a570c03e";
sums["${OUT_PATH}/outh.wav"]="576409e4a3cd5e76950aa0134389d75a";
sums["${OUT_PATH}/outi.wav"]="07e31be2ff4f16b91adcf540a570c03e";

sums["${OUT_PATH}/outd-B.wav"]="d51e36787d2cf8a10be87a1e123bb976";
sums["${OUT_PATH}/outf-B.wav"]="07e31be2ff4f16b91adcf540a570c03e";
sums["${OUT_PATH}/outh-B.wav"]="576409e4a3cd5e76950aa0134389d75a";
sums["${OUT_PATH}/outi-B.wav"]="07e31be2ff4f16b91adcf540a570c03e";

sums["${OUT_PATH}/outi16.wav"]="9f21f81dd274b3695adbb0418f787b48";
sums["${OUT_PATH}/outu8.wav"]="18f1c6cbe373121a3f4c1bfe9f282467";

function cleanup {
  for i in "${!sums[@]}"; do
    rm "$i";
  done
}
trap cleanup EXIT;

TEMP=$DSD_CMD
export DSD_CMD="${DSD_CMD} -f1";
coproc SIMO {
  time ./example_simo.sh -i /mnt/d/uint8.wav --vfos=15000,-60000 -w5k -c-3.5E+5 -t155.685M -vv -d64 2>&1
}

ts="";
while IFS= ; read -r line; do
  if [[ $line == *"real"* ]] || [[ $line == *"user"* ]] || [[ $line == *"sys"* ]]; then
    echo $line;
  elif [[ $line == *"timestamp"* ]]; then
    ts=$(echo $line | grep "timestamp" - | sed -E "s/^.*: timestamp: ([0-9]+)$/\1/g");
    echo "${OUT_PATH}/out-155625000-${ts}.wav";
    echo "${OUT_PATH}/out-155685000-${ts}.wav";
    echo "${OUT_PATH}/out-155700000-${ts}.wav";
  fi
done <&"${SIMO[0]}"

sums["${OUT_PATH}/out-155625000-${ts}.wav"]="38acd5677b3e813eea185523d47b9076";
sums["${OUT_PATH}/out-155685000-${ts}.wav"]="4cae5a0dfbbe4bd06ea4de41988bd606";
sums["${OUT_PATH}/out-155700000-${ts}.wav"]="2eaa5e1e736f3b68e67c3b89d1407e1e";

wait $SIMO_PID;
echo "sdrterm returned: ${?}";
export DSD_CMD="${TEMP} -fr";

./example.sh /mnt/d/SDRSharp_20160101_231914Z_12kHz_IQ.wav;

declare -A z="( `sed -E "s/^((\d|\w)+)\s*((\d|\w|\/|\-|\.)+)$/[\3]=\1/g" <<< $(md5sum ${OUT_PATH}/*.wav)` )";
for i in "${!sums[@]}"; do
  [[ "${sums["$i"]}" == "${z["$i"]}" ]] && echo "checksum matched: ${i}" || echo "FAILED: ${i}";
done

exit;
