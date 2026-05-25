from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ai_projects.research_agent import main


if __name__ == "__main__":
    main()
