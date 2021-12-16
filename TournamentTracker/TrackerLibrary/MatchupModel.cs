namespace TrackerLibrary
{
    public class MatchupModel
    {
        /// <summary>
        /// Represents the teams in one match-up.
        /// </summary>
        public List<MatchupEntryModel> Entries { get; set; } = new List<MatchupEntryModel>();

        /// <summary>
        /// Represents the winner for this particular match-up.
        /// </summary>
        public TeamModel Winner { get; set; }

        /// <summary>
        /// Represents the current round.
        /// </summary>
        public int MatchupRound { get; set; }
    }
}