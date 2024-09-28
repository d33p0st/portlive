from portlive import portlive

def test_():
    with portlive(['wrapper_bar.wrapper', 'requests'], ['wrapper', 'rr']) as pl:
        try:
            a =  pl.wrapper.Wrapper()
            b = pl.rr.get('https://github.com')
            assert b.status_code == 200
            return
        except Exception:
            assert False