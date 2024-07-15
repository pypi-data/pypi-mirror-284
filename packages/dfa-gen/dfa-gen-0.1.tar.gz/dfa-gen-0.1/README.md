## dfa-gen

### 1. description

- protein sequence와 utr을 입력하면 [LinearDesign](https://github.com/LinearDesignSoftware/LinearDesign)에서 사용할 수 있는 DFA를 생성하고 이를 시각화한 graph를 생성합니다.
- 본 package로 만들어진 DFA는 <U>수정된 LinearDesign 프로그램에서만</U> 사용할 수 있습니다.
- graph 예시 이미지 (`dfa-gen "MA" -l 3 -u UGGACGA`의 결과)

### 2. pre-requirement

```
pandas
graphviz
```

### 3. to run

- `git clone`을 통해 본 package를 내려받았다면, root에서 다음의 명령어를 먼저 실행해주세요. (root =`setup.py`가 있는 위치)
  ```
  pip install .
  ```
- 이후에는 다음의 명령어와 옵션으로 실행가능합니다. 이미지를 포함한 결과 파일 `test` 디렉토리에 저장됩니다.
  ```
  dfa-gen [PROTEIN_SEQUENCE] [OPTIONS]
  ```
- options
  1.  `--utr` 옵션을 사용하면 nucleotide sequence를 넘겨줄 수 있습니다. (default: empty string)
      ```
      --utr [UTR_SEQUENCE] or -u [UTR_SEQUENCE]
      ```
  2.  `--lambda` 옵션을 사용하면 가중치 계산에 사용될 lambda 값을 지정할 수 있습니다. (default: 0)
      ```
      --lambda_val [LAMBDA] or -l [LAMBDA]
      ```
- example
  ```
  dfa-gen METFWPLPAW -u UGGACGA
  dfa-gen "MEFA" -l 3 -u UGGACGA
  ```
