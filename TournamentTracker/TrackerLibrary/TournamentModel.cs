namespace TrackerLibrary
{
    public class TournamentModel
    {
        /// <summary>
        /// Represents the Tournament name.
        /// </summary>
        public string TournamentName { get; set; }

        /// <summary>
        /// Represent the entry fee for this tournament.
        /// </summary>
        public decimal EntryFee { get; set; }

        /// <summary>
        /// Represents all teams in this Tournament.
        /// </summary>
        public List<TeamModel> EnteredTeams { get; set; } = new List<TeamModel>();

        /// <summary>
        /// Represents all prizes.
        /// </summary>
        public List<PrizeModel> Prizes { get; set; } = new List<PrizeModel>();

        /// <summary>
        /// Represents all match-ups in all rounds.
        /// </summary>
        public List<List<MatchupModel>> Rounds { get; set; } = new List<List<MatchupModel>>();
    }
}
