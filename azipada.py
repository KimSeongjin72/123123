name: Test Action
on: [push]

jobs:
  get-num-square:
    runs-on: ubuntu-latest
      name: return the number square
      steps:
        -name: Checkout
         uses: actions/checkout@v2
        -name: Fetch num squared
         id: get_square
         uses: ./
         with:
          num: 11
        -name: Print the square
         run: echo "${{ steps.get_square.outputs.num_squared }}"
