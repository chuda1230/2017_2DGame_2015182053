# -*- mode: python -*-

block_cipher = None


a = Analysis(['2015182053_2DGP.py'],
             pathex=['D:\\2DGame\\2017_2DGame_2015182053\\project'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='2015182053_2DGP',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
