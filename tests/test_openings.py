from app import classify_opening

def test_c50():
    sample_pgn = '''
    [Event "European Club Cup"]
    [Site "Izmir TUR"]
    [Date "2004.10.05"]
    [EventDate "2004.10.03"]
    [Round "3"]
    [Result "1-0"]
    [White "Nigel Short"]
    [Black "Aleksej Gennadyevich Aleksandrov"]
    [ECO "C50"]
    [WhiteElo "2687"]
    [BlackElo "2659"]
    [PlyCount "85"]

    1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. Nc3 Nf6 5. d3 d6 6. Bg5 h6
    7. Bxf6 Qxf6 8. Nd5 Qd8 9. c3 a6 10. d4 Ba7 11. dxe5 Nxe5
    12. Nxe5 dxe5 13. Qh5 O-O 14. Qxe5 Re8 15. Qf4 Qd6 16. Qxd6
    Rxe4+ 17. Ne3 cxd6 18. Bd5 Re5 19. O-O-O Bxe3+ 20. fxe3 Rxe3
    21. Rhf1 Be6 22. Bxb7 Ra7 23. Bd5 a5 24. Bxe6 Rxe6 25. Rd2 a4
    26. Kc2 g5 27. Rf5 Kg7 28. Rfd5 Ra6 29. Kd3 f6 30. Kc4 Rb6
    31. Ra5 Re4+ 32. Kd3 Rg4 33. Rf2 Kg6 34. h3 Rh4 35. Raf5 Rf4
    36. R5xf4 gxf4 37. Ke4 Kg5 38. Rd2 f5+ 39. Kf3 Rc6 40. a3 Rb6
    41. h4+ Kxh4 42. Kxf4 d5 43. Rd3 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "C50"
    assert opening_name == "Italian Game"

def test_c20():
    sample_pgn = '''
    [Event "Rome"]
    [Site "Rome ITA"]
    [Date "1560.??.??"]
    [EventDate "1560.??.??"]
    [Round "?"]
    [Result "1-0"]
    [White "Ruy Lopez de Segura"]
    [Black "Giovanni Leonardo Di Bona da Cutri"]
    [ECO "C20"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "18"]

    1.e4 e5 2.Nf3 f6 3.Nxe5 fxe5 4.Qh5+ g6 5.Qxe5+ Qe7 6.Qxh8 Nf6
    7.d4 Kf7 8.Bc4+ d5 9.Bxd5+ Nxd5 {and White goes on to win.}
    1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "C20"
    assert opening_name == "King's Pawn Game"

def test_c60():
    sample_pgn = '''
    [Event "Staunton - Horwitz m"]
    [Site "London ENG"]
    [Date "1846.02.02"]
    [EventDate "1846.02.02"]
    [Round "1"]
    [Result "1-0"]
    [White "Howard Staunton"]
    [Black "Bernhard Horwitz"]
    [ECO "C60"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [Source "Illustrated London News, 1846.02.07, p.99"]
    [PlyCount "73"]

    1.e4 e5 2.Nf3 Nc6 3.Bb5 Qf6 4.Nc3 Bd6 5.Nd5 Qg6 6.d3 Nce7
    7.Nh4 Qe6 8.Ne3 Bc5 9.Bc4 Qf6 10.Nf3 d6 11.c3 Nh6 12.O-O Bg4
    13.Nxg4 Nxg4 14.a4 a5 15.Bd2 Qg6 16.h3 Nf6 17.d4 exd4 18.cxd4
    Bb6 19.e5 Nd7 20.Qe2 d5 21.Bd3 Qh5 22.Kh2 f5 23.exf6 Nxf6
    24.Rae1 Nfg8 25.Bg5 Qf7 26.Ne5 Qe6 27.Qh5+ Kf8 28.Ng6+ hxg6
    29.Qxh8 Qd6+ 30.f4 Re8 31.Re2 Bxd4 32.Rfe1 Kf7 33.Qh7 Nf6
    34.Rxe7+ Rxe7 35.Bxg6+ Kf8 36.Qh8+ Ng8 37.Bxe7+ 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "C60"
    assert opening_name == "Ruy Lopez"

def test_d10():
    sample_pgn = '''
    [Event "Launceston CC v Green Ponds CC corr match"]
    [Site "corr"]
    [Date "1848.??.??"]
    [EventDate "1848.??.??"]
    [Round "2"]
    [Result "1-0"]
    [White "Green Ponds Chess Club"]
    [Black "Launceston Chess Club"]
    [ECO "D10"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "69"]
    [SiteNote "Tasmania, Australia"]

    1. d4 d5 2. c4 c6 3. e3 f6 4. Nc3 e6 5. a3 g6 6. f4 f5 7. Nf3
    Nf6 8. Bd2 Ne4 9. Nxe4 fxe4 10. Ne5 Bg7 11. h4 Bxe5 12. fxe5
    h5 13. Bb4 b6 14. Bd6 Nd7 15. g3 Bb7 16. Bg2 c5 17. O-O Qc8
    18. Rf2 Qc6 19. Qf1 cxd4 20. exd4 e3 21. Rf7 Qc8 22. Bf3 dxc4
    23. Bxb7 Qxb7 24. Rg7 Kd8 25. Qf7 Re8 26. Rg8 Rxg8 27. Qxg8+
    Nf8 28. Qxf8+ Kd7 29. Qe7+ Kc6 30. Qxe6 Qc8 31. Qxc4+ Kb7
    32. Qf7+ Ka6 33. Qf1+ b5 34. a4 Kb6 35. Qxb5# 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "D10"
    assert opening_name == "Queen's Gambit Declined"

def test_e60():
    sample_pgn = '''
    [Event "Mannheim"]
    [Site "Mannheim GER"]
    [Date "1914.07.28"]
    [EventDate "1914.07.20"]
    [Round "7"]
    [Result "1-0"]
    [White "Alfred Ehrhardt Post"]
    [Black "Jacques Mieses"]
    [ECO "E60"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "45"]

    1.d4 Nf6 2.Nf3 g6 3.c4 c5 4.d5 d6 5.Nc3 Bg7 6.e4 O-O 7.Bd3 e5
    8.h3 Na6 9.Be3 Bd7 10.Qd2 Qc7 11.g4 Nxe4 12.Bxe4 f5 13.gxf5
    gxf5 14.Bh6 fxe4 15.Rg1 Rf7 16.Bxg7 Rxg7 17.Rxg7+ Kxg7 18.Qg5+
    Kf7 19.Nxe4 Rf8 20.O-O-O Bxh3 21.Qf6+ Ke8 22.Nxd6+ Kd7
    23.Nxe5# 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "E60"
    assert opening_name == "King's Indian Defense"

def test_b01():
    sample_pgn = '''
    [Event "Biel Credit Suisse"]
    [Site "Biel SUI"]
    [Date "1997.07.21"]
    [EventDate "?"]
    [Round "1"]
    [Result "1-0"]
    [White "Viswanathan Anand"]
    [Black "Joel Lautier"]
    [ECO "B01"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "49"]

    1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 c6 6.Bc4 Bf5
    7.Ne5 e6 8.g4 Bg6 9.h4 Nbd7 10.Nxd7 Nxd7 11.h5 Be4 12.Rh3 Bg2
    13.Re3 Nb6 14.Bd3 Nd5 15.f3 Bb4 16.Kf2 Bxc3 17.bxc3 Qxc3
    18.Rb1 Qxd4 19.Rxb7 Rd8 20.h6 gxh6 21.Bg6 Ne7 22.Qxd4 Rxd4
    23.Rd3 Rd8 24.Rxd8+ Kxd8 25.Bd3 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "B01"
    assert opening_name == "Scandinavian Defense"

def test_b20():
    sample_pgn = '''
    [Event "Miscellaneous Game"]
    [Site "?"]
    [Date "1620.??.??"]
    [EventDate "?"]
    [Round "31"]
    [Result "1-0"]
    [White "Gioachino Greco"]
    [Black "NN"]
    [ECO "B20"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "63"]

    1.e4 c5 2.b4 cxb4 3.d4 e6 4.a3 bxa3 5.c4 Bb4+ 6.Bd2 Bxd2+
    7.Qxd2 d5 8.e5 dxc4 9.Bxc4 Nc6 10.Ne2 Nge7 11.Rxa3 O-O 12.O-O
    Nf5 13.Rd3 a6 14.f4 b5 15.Bb3 a5 16.g4 Nh6 17.h3 a4 18.Bc2 b4
    19.f5 exf5 20.g5 b3 21.Bd1 Qa5 22.Qf4 Qb5 23.Rg3 Bd7 24.gxh6
    g6 25.Qg5 f6 26.exf6 Rf7 27.Nf4 Nxd4 28.Nxg6 Ne6 29.Ne7+ Kh8
    30.Qg7+ Nxg7 31.fxg7+ Rxg7 32.hxg7# 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "B20"
    assert opening_name == "Sicilian Defense"

def test_unknown():
    sample_pgn = '''
    [Event "Amsterdam"]
    [Site "Amsterdam NED"]
    [Date "1851.??.??"]
    [EventDate "?"]
    [Round "?"]
    [Result "1-0"]
    [White "Maarten van 't Kruijs"]
    [Black "Klaas de Heer"]
    [ECO "A01"]
    [WhiteElo "?"]
    [BlackElo "?"]
    [PlyCount "54"]
    [Source "Sissa, v5, 1851, pp280-281"]

    1. b3 e5 2. Bb2 Nc6 3. g3 d5 4. Bg2 Nf6 5. e3 Bf5 6. d3 Bc5
    7. Ne2 Qd6 8. c3 Rd8 9. O-O O-O 10. a3 a6 11. d4 exd4 12. cxd4
    Bb6 13. b4 Ne7 14. Nbc3 Ba7 15. f3 Qe6 16. Qd2 Rfe8 17. Nf4
    Qc6 18. Kh1 Nc8 19. Rfe1 Nb6 20. Bf1 Nc4 21. Bxc4 dxc4 22. d5
    g5 23. e4 Bg6 24. Nxg6 hxg6 25. Qxg5 Qd6 26. Nb5 axb5 27. Bxf6
    Rd7 1-0
    '''
    
    eco_code, opening_name = classify_opening(sample_pgn)
    
    assert eco_code == "A00"
    assert opening_name == "Uncommon Opening"