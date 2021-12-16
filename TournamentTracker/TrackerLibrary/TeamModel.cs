namespace TrackerLibrary
{
    public class TeamModel
    {
        /// <summary>
        /// Represents all members in particular team.
        /// </summary>
        public List<PersonModel> TeamMembers { get; set; } = new List<PersonModel>();

        /// <summary>
        /// Represents the name for particular team.
        /// </summary>
        public string TeamName { get; set; }
    }
}