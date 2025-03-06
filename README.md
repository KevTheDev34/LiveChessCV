# LiveChessCV

## Objectives
- [x] Get camera view of chessboard  
    - Used OpenCV to get a live video feed from my webcam. 
- [x] Detect board itself 
    - Used an example (I don't remember from where) to run the chessboard detector. Then brought up my chessboard to the camera, overlayed a square around the detected chessboard.
- [ ] Detect squares with in board, associate letters & numbers to squares  
- [ ] Detect pieces  
- [ ] Associate pieces to squares  
- [ ] Adjust orientation of board markings to orientation of pieces (set right sides of the board to where white and black should be)  
- [ ] After spacebar press, detect change of positions  
- [ ] Record change of positions in chess notation  
- [ ] On start of program, create a text file in a predetermined folder (Matches)  
  - [ ] Title text file in the following format: `YYYYMMDD_matchNNN_W/B.txt`  
    - [ ] Get `NNN` by checking the number of files in the Matches folder  
    - [ ] `W` for white winning or `B` for black winning, not both  
  - [ ] Populate file in PGN notation:  
    - [ ] Populate metadata text variable for use after the analysis is finished:  
      - Event: `"Live Chess"`  
      - Site: `(get_address)`  
      - Date: `(get_date in YYYY.MM.DD format)`  
      - White: `(white_player)`  
      - Black: `(black_player)`  
      - Termination: `"{winner} won by checkmate"`  
      - [Later add a button to resign and a button to draw]  

- [ ] After checkmate  
  - [ ] Hold winner in `winner` variable  
  - [ ] Prompt user to input who played black and white (`"White: ____"` `"Black: ____"`) and hold values for `UpdateMetadata()`  
  - [ ] Save but do not close this file  
  - [ ] Upload to Chess.com for analysis; file should only have move text  

- [ ] Sleep/wait until the analysis finishes  
  - [ ] Find a way to determine if the analysis has finished and check for that every ten seconds  

- [ ] Once analysis finishes  
  - [ ] Extract ELO for each player and hold in `white_elo`, `black_elo`  
  - [ ] Update placeholders in PGN metadata using `UpdateMetadata()`  
  - [ ] Save and close PGN, end of program  

## Notes
- [ ] Theoretically, this should work for both live games and virtual games. I don’t actually detect the pieces themselves, I’m tracking the change of position of a piece relative to the position on the board. The thing in the square can be anything as long as it remains consistent.  

## References
- [Chess Notation](https://www.chess.com/terms/chess-notation)  
- [PGN Format](https://www.chess.com/terms/chess-pgn)  
- [Chess Analysis](https://www.chess.com/analysis?tab=analysis)  
