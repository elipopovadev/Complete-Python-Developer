namespace TrackerUI
{
    partial class TournamentViewerForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TournamentViewerForm));
            this.headerLabel = new System.Windows.Forms.Label();
            this.tournamentName = new System.Windows.Forms.Label();
            this.round = new System.Windows.Forms.Label();
            this.roundDropDown = new System.Windows.Forms.ComboBox();
            this.unplayedOnlyCheckBox = new System.Windows.Forms.CheckBox();
            this.matchupListBox = new System.Windows.Forms.ListBox();
            this.teamOneName = new System.Windows.Forms.Label();
            this.teamOneScoreLabel = new System.Windows.Forms.Label();
            this.teamOneScoreValue = new System.Windows.Forms.TextBox();
            this.teamTwoScoreValue = new System.Windows.Forms.TextBox();
            this.teamTwoScoreLabel = new System.Windows.Forms.Label();
            this.teamTwoName = new System.Windows.Forms.Label();
            this.versusLabel = new System.Windows.Forms.Label();
            this.scoreButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // headerLabel
            // 
            this.headerLabel.AutoSize = true;
            this.headerLabel.ForeColor = System.Drawing.SystemColors.Highlight;
            this.headerLabel.Location = new System.Drawing.Point(14, 35);
            this.headerLabel.Margin = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.headerLabel.Name = "headerLabel";
            this.headerLabel.Size = new System.Drawing.Size(271, 62);
            this.headerLabel.TabIndex = 0;
            this.headerLabel.Text = "Tournament:";
            this.headerLabel.UseWaitCursor = true;
            // 
            // tournamentName
            // 
            this.tournamentName.AutoSize = true;
            this.tournamentName.ForeColor = System.Drawing.SystemColors.Highlight;
            this.tournamentName.Location = new System.Drawing.Point(270, 35);
            this.tournamentName.Margin = new System.Windows.Forms.Padding(5, 0, 5, 0);
            this.tournamentName.Name = "tournamentName";
            this.tournamentName.Size = new System.Drawing.Size(189, 62);
            this.tournamentName.TabIndex = 1;
            this.tournamentName.Text = "<none>";
            this.tournamentName.UseWaitCursor = true;
            // 
            // round
            // 
            this.round.AutoSize = true;
            this.round.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.round.ForeColor = System.Drawing.SystemColors.Highlight;
            this.round.Location = new System.Drawing.Point(27, 147);
            this.round.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.round.Name = "round";
            this.round.Size = new System.Drawing.Size(111, 45);
            this.round.TabIndex = 2;
            this.round.Text = "Round";
            this.round.UseWaitCursor = true;
            // 
            // roundDropDown
            // 
            this.roundDropDown.FormattingEnabled = true;
            this.roundDropDown.Location = new System.Drawing.Point(138, 130);
            this.roundDropDown.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.roundDropDown.Name = "roundDropDown";
            this.roundDropDown.Size = new System.Drawing.Size(265, 70);
            this.roundDropDown.TabIndex = 3;
            this.roundDropDown.UseWaitCursor = true;
            // 
            // unplayedOnlyCheckBox
            // 
            this.unplayedOnlyCheckBox.AutoSize = true;
            this.unplayedOnlyCheckBox.Font = new System.Drawing.Font("Segoe UI Light", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.unplayedOnlyCheckBox.ForeColor = System.Drawing.SystemColors.Highlight;
            this.unplayedOnlyCheckBox.Location = new System.Drawing.Point(138, 206);
            this.unplayedOnlyCheckBox.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.unplayedOnlyCheckBox.Name = "unplayedOnlyCheckBox";
            this.unplayedOnlyCheckBox.Size = new System.Drawing.Size(209, 42);
            this.unplayedOnlyCheckBox.TabIndex = 4;
            this.unplayedOnlyCheckBox.Text = "Unplayed only";
            this.unplayedOnlyCheckBox.UseVisualStyleBackColor = true;
            this.unplayedOnlyCheckBox.UseWaitCursor = true;
            this.unplayedOnlyCheckBox.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // matchupListBox
            // 
            this.matchupListBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.matchupListBox.FormattingEnabled = true;
            this.matchupListBox.ItemHeight = 62;
            this.matchupListBox.Location = new System.Drawing.Point(27, 337);
            this.matchupListBox.Name = "matchupListBox";
            this.matchupListBox.Size = new System.Drawing.Size(376, 374);
            this.matchupListBox.TabIndex = 5;
            this.matchupListBox.UseWaitCursor = true;
            // 
            // teamOneName
            // 
            this.teamOneName.AutoSize = true;
            this.teamOneName.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.teamOneName.ForeColor = System.Drawing.SystemColors.Highlight;
            this.teamOneName.Location = new System.Drawing.Point(551, 356);
            this.teamOneName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.teamOneName.Name = "teamOneName";
            this.teamOneName.Size = new System.Drawing.Size(195, 45);
            this.teamOneName.TabIndex = 6;
            this.teamOneName.Text = "<team one>";
            this.teamOneName.UseWaitCursor = true;
            // 
            // teamOneScoreLabel
            // 
            this.teamOneScoreLabel.AutoSize = true;
            this.teamOneScoreLabel.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.teamOneScoreLabel.ForeColor = System.Drawing.SystemColors.Highlight;
            this.teamOneScoreLabel.Location = new System.Drawing.Point(539, 405);
            this.teamOneScoreLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.teamOneScoreLabel.Name = "teamOneScoreLabel";
            this.teamOneScoreLabel.Size = new System.Drawing.Size(97, 45);
            this.teamOneScoreLabel.TabIndex = 7;
            this.teamOneScoreLabel.Text = "Score";
            this.teamOneScoreLabel.UseWaitCursor = true;
            // 
            // teamOneScoreValue
            // 
            this.teamOneScoreValue.Location = new System.Drawing.Point(634, 405);
            this.teamOneScoreValue.Name = "teamOneScoreValue";
            this.teamOneScoreValue.Size = new System.Drawing.Size(129, 70);
            this.teamOneScoreValue.TabIndex = 8;
            this.teamOneScoreValue.UseWaitCursor = true;
            // 
            // teamTwoScoreValue
            // 
            this.teamTwoScoreValue.Location = new System.Drawing.Point(634, 599);
            this.teamTwoScoreValue.Name = "teamTwoScoreValue";
            this.teamTwoScoreValue.Size = new System.Drawing.Size(129, 70);
            this.teamTwoScoreValue.TabIndex = 11;
            this.teamTwoScoreValue.UseWaitCursor = true;
            // 
            // teamTwoScoreLabel
            // 
            this.teamTwoScoreLabel.AutoSize = true;
            this.teamTwoScoreLabel.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.teamTwoScoreLabel.ForeColor = System.Drawing.SystemColors.Highlight;
            this.teamTwoScoreLabel.Location = new System.Drawing.Point(539, 599);
            this.teamTwoScoreLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.teamTwoScoreLabel.Name = "teamTwoScoreLabel";
            this.teamTwoScoreLabel.Size = new System.Drawing.Size(97, 45);
            this.teamTwoScoreLabel.TabIndex = 10;
            this.teamTwoScoreLabel.Text = "Score";
            this.teamTwoScoreLabel.UseWaitCursor = true;
            // 
            // teamTwoName
            // 
            this.teamTwoName.AutoSize = true;
            this.teamTwoName.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.teamTwoName.ForeColor = System.Drawing.SystemColors.Highlight;
            this.teamTwoName.Location = new System.Drawing.Point(551, 550);
            this.teamTwoName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.teamTwoName.Name = "teamTwoName";
            this.teamTwoName.Size = new System.Drawing.Size(192, 45);
            this.teamTwoName.TabIndex = 9;
            this.teamTwoName.Text = "<team two>";
            this.teamTwoName.UseWaitCursor = true;
            this.teamTwoName.Click += new System.EventHandler(this.teamTwoName_Click);
            // 
            // versusLabel
            // 
            this.versusLabel.AutoSize = true;
            this.versusLabel.Font = new System.Drawing.Font("Segoe UI Light", 19.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.versusLabel.ForeColor = System.Drawing.SystemColors.Highlight;
            this.versusLabel.Location = new System.Drawing.Point(653, 499);
            this.versusLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.versusLabel.Name = "versusLabel";
            this.versusLabel.Size = new System.Drawing.Size(81, 45);
            this.versusLabel.TabIndex = 12;
            this.versusLabel.Text = "-VS-";
            this.versusLabel.UseWaitCursor = true;
            // 
            // scoreButton
            // 
            this.scoreButton.FlatAppearance.BorderColor = System.Drawing.Color.Silver;
            this.scoreButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(102)))), ((int)(((byte)(102)))), ((int)(((byte)(102)))));
            this.scoreButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(242)))), ((int)(((byte)(242)))), ((int)(((byte)(242)))));
            this.scoreButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.scoreButton.Font = new System.Drawing.Font("Segoe UI Semibold", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.scoreButton.ForeColor = System.Drawing.SystemColors.Highlight;
            this.scoreButton.Location = new System.Drawing.Point(797, 499);
            this.scoreButton.Name = "scoreButton";
            this.scoreButton.Size = new System.Drawing.Size(191, 71);
            this.scoreButton.TabIndex = 13;
            this.scoreButton.Text = "Score";
            this.scoreButton.UseVisualStyleBackColor = true;
            this.scoreButton.UseWaitCursor = true;
            // 
            // TournamentViewerForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(25F, 62F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1355, 708);
            this.Controls.Add(this.scoreButton);
            this.Controls.Add(this.versusLabel);
            this.Controls.Add(this.teamTwoScoreValue);
            this.Controls.Add(this.teamTwoScoreLabel);
            this.Controls.Add(this.teamTwoName);
            this.Controls.Add(this.teamOneScoreValue);
            this.Controls.Add(this.teamOneScoreLabel);
            this.Controls.Add(this.teamOneName);
            this.Controls.Add(this.matchupListBox);
            this.Controls.Add(this.unplayedOnlyCheckBox);
            this.Controls.Add(this.roundDropDown);
            this.Controls.Add(this.round);
            this.Controls.Add(this.tournamentName);
            this.Controls.Add(this.headerLabel);
            this.Font = new System.Drawing.Font("Segoe UI Light", 28.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(51)))), ((int)(((byte)(153)))), ((int)(((byte)(255)))));
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(11, 10, 11, 10);
            this.Name = "TournamentViewerForm";
            this.Text = "Tournament Viewer";
            this.UseWaitCursor = true;
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label headerLabel;
        private Label tournamentName;
        private Label round;
        private ComboBox roundDropDown;
        private CheckBox unplayedOnlyCheckBox;
        private ListBox matchupListBox;
        private Label teamOneName;
        private Label teamOneScoreLabel;
        private TextBox teamOneScoreValue;
        private TextBox teamTwoScoreValue;
        private Label teamTwoScoreLabel;
        private Label teamTwoName;
        private Label versusLabel;
        private Button scoreButton;
    }
}