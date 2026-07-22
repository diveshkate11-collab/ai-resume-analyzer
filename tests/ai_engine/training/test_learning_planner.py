from app.ai_engine.training.learning_planner import LearningPlanner


def test_learning_plan_multiple_skills():
    result = LearningPlanner.create(
        [
            "Git",
            "SQL",
            "Docker",
        ]
    )

    assert len(result) == 3
    assert result[0] == "Week 1: Learn Git"
    assert result[1] == "Week 2: Learn SQL"
    assert result[2] == "Week 3: Learn Docker"


def test_learning_plan_single_skill():
    result = LearningPlanner.create(
        [
            "Python",
        ]
    )

    assert result == [
        "Week 1: Learn Python",
    ]


def test_learning_plan_empty():
    result = LearningPlanner.create([])

    assert result == []