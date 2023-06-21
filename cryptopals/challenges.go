package main

func RunChallenge(set int, challenge int) string {
	switch set {
	case 1:
		return RunChallengeSetOne(challenge)
	default:
		return "No set found"
	}
}

// TODO: maybe these should run as unit tests instead? Consider deleting.
func RunChallengeSetOne(challenge int) string {
	switch challenge {
	case 1:
		return "Hello world"
	default:
		return "No challenge found"
	}
}
