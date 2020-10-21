using UnityEngine;

[CreateAssetMenu(menuName = nameof(State))]
public class State : ScriptableObject
{
    [SerializeField]
    [TextArea(14,10)]
    string storyText;

    [SerializeField]
    State[] nextStates;

    public string GetStateStory()
    {
        return this.storyText;
    }

    public State[] GetNextStates()
    {
        return this.nextStates;
    }

}
