# Installing Poppler for Windows

For PDF to image conversion to work properly, you need to install **poppler-utils**.

## Option 1: Download Pre-built Binaries (Recommended)

1. **Download poppler for Windows:**
   - Go to: https://github.com/oschwartz10612/poppler-windows/releases
   - Download the latest `Release-XX.XX.X-X.zip` file

2. **Extract and Install:**
   - Extract the ZIP file to a folder like `C:\poppler`
   - Add `C:\poppler\Library\bin` to your system PATH

3. **Add to PATH:**
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Click "Environment Variables"
   - Under "System Variables", find and select "Path", click "Edit"
   - Click "New" and add: `C:\poppler\Library\bin`
   - Click "OK" to save

## Option 2: Using Conda (if you have Anaconda/Miniconda)

```bash
conda install -c conda-forge poppler
```

## Option 3: Using Chocolatey (if you have Chocolatey)

```bash
choco install poppler
```

## Verify Installation

After installation, restart your command prompt and test:

```bash
pdftoppm -h
```

If this shows help text, poppler is installed correctly.

## Alternative: Simple PDF Text Processing

If you don't want to install poppler, the system will still work but won't be able to convert scanned PDFs to images. It will only extract text from digital PDFs.
