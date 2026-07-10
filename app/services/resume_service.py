from pathlib import Path
import shutil

from fastapi import HTTPException, UploadFile

from app.ai_engine.parser.resume_parser import ResumeParser


class ResumeService:
    """
    Handles resume upload and analysis.
    """

    UPLOAD_DIR = Path("uploads/resumes")
    ALLOWED_EXTENSIONS = {".pdf", ".docx"}

    @classmethod
    def upload_and_analyze(cls, file: UploadFile):
        """
        Validate, save, and analyze the uploaded resume.
        """

        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        extension = Path(file.filename).suffix.lower()

        if extension not in cls.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed.",
            )

        file_path = cls.UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        analysis = ResumeParser.extract(str(file_path))

        return {
            "success": True,
            "filename": file.filename,
            "message": "Resume uploaded and analyzed successfully.",
            "analysis": analysis,
        }