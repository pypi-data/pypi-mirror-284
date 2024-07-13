import typer
import ocr_map as om

app = typer.Typer()

@app.callback()
def callback():
  ...

@app.command('fit')
def fit(
  pickle_output: str,
  labels: str = typer.Option(..., '-l', '--labels', help='Labels file, one label per line'),
  preds: str = typer.Option(..., '-p', '--preds', help='Preds NDJSON file, one prediction per line'),
  verbose: bool = typer.Option(False, '-v', '--verbose'),
):
  if verbose:
    print('Parsing samples...')
  from .parse import parse_lines
  with open(labels) as labs_f, open(preds) as preds_f:
    samples = list(parse_lines(labs_f, preds_f))
  
  if verbose:
    print(f'Parsed {len(samples)} samples. Fitting model...')
  model = om.Model.fit(samples)
  if verbose:
    print(f'Saving model to {pickle_output}...')
  import pickle
  with open(pickle_output, 'wb') as f:
    pickle.dump(model, f)