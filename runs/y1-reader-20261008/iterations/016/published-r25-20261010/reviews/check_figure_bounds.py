from pathlib import Path
import io,hashlib,json,contextlib
import matplotlib
matplotlib.use('Agg')
from matplotlib.figure import Figure
from matplotlib.text import Text
p=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
original_save=Figure.savefig
original_draw=Text.draw
current={'path':None,'texts':[]}
records=[]
def draw(self,renderer):
    if current['path'] and self.get_visible() and self.get_text():
        box=self.get_window_extent(renderer)
        current['texts'].append({'text':self.get_text(),'bounds':[box.x0,box.y0,box.x1,box.y1],'canvas':[renderer.width,renderer.height],'outside':bool(box.x0<0 or box.y0<0 or box.x1>renderer.width or box.y1>renderer.height)})
    return original_draw(self,renderer)
def save(self,fname,*args,**kwargs):
    current['path']=str(fname); current['texts']=[]
    data=io.BytesIO()
    original_save(self,data,*args,format='png',**kwargs)
    data=data.getvalue()
    outside=[r for r in current['texts'] if r['outside']]
    records.append({'file':str(Path(fname).relative_to(p)),'recreated_sha256':hashlib.sha256(data).hexdigest(),'exact_frozen_png_recreated_in_memory':data==Path(fname).read_bytes(),'text_outside_canvas':outside})
    current['path']=None
Figure.savefig=save
Text.draw=draw
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile((p/'author/create_figures.py').read_text(),str(p/'author/create_figures.py'),'exec'),{'__name__':'__main__'})
result={'method':'Replay the unchanged figure source with savefig redirected to BytesIO only; inspect Text artist bounds during actual Agg draw at original180dpi. Compare each in-memory PNG against unchanged frozen file bytes. No teaching/output file written.','records':records}
(p/'reviews/figure-bounds.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
