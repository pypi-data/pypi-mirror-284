#include "CLink.h"

CLink::CLink(int numPlayers, double* coalitionValues, int minNumberOfPlayersPerGroup, int maxNumberOfPlayersPerGroup) 
{
	this->numPlayers = numPlayers;
	this->coalitionValues = coalitionValues;
	this->minNumberOfPlayersPerGroup = minNumberOfPlayersPerGroup;
	this->maxNumberOfPlayersPerGroup = maxNumberOfPlayersPerGroup;

	this->minNumGroups = numPlayers / maxNumberOfPlayersPerGroup;
	this->maxNumGroups = (unsigned int)(floor(numPlayers / minNumberOfPlayersPerGroup));

	this->PL.resize(numPlayers);
	for (int i = 0; i < numPlayers; i++)
		this->PL[i].resize(numPlayers);

	this->optimalCSInBitFormat.resize(numPlayers);
	for (int i = 0; i < numPlayers; i++)
		this->optimalCSInBitFormat[i] = 1 << i;
}

void CLink::CLinkAlgorithm()
{
	initializePL();

	int bestIndexI = 0; int bestIndexJ = 0;
	double bestPairValue = -10;

	for (unsigned int i = 0; i < numPlayers; i++) {
		for (unsigned int j = 0; j < numPlayers; j++)
		{
			if (PL[i][j] > bestPairValue)
			{
				bestIndexI = i;
				bestIndexJ = j;
				bestPairValue = PL[i][j];
			}
		}
	}

	bool coalitionsCanBeMerged = true;

	while (coalitionsCanBeMerged && (optimalCSInBitFormat.size() > maxNumGroups))
	{
		coalitionsCanBeMerged = false;


		// Remove the two coalitions that should be merged and add the merged coalition
		int newCS = optimalCSInBitFormat[bestIndexI] ^ optimalCSInBitFormat[bestIndexJ];
		if (bestIndexI > bestIndexJ) 
		{
			optimalCSInBitFormat.erase(optimalCSInBitFormat.begin() + bestIndexI);
			optimalCSInBitFormat.erase(optimalCSInBitFormat.begin() + bestIndexJ);
		}
		else
		{
			optimalCSInBitFormat.erase(optimalCSInBitFormat.begin() + bestIndexJ);
			optimalCSInBitFormat.erase(optimalCSInBitFormat.begin() + bestIndexI);
		}

		optimalCSInBitFormat.push_back(newCS);

		// Update PL, first erase lines of old coalitions, then columns
		if (bestIndexI > bestIndexJ)
		{
			PL.erase(PL.begin() + bestIndexI);
			PL.erase(PL.begin() + bestIndexJ);
		}
		else
		{
			PL.erase(PL.begin() + bestIndexJ);
			PL.erase(PL.begin() + bestIndexI);
		}

		PL.resize(optimalCSInBitFormat.size());
		int posOfNewCS = (int)optimalCSInBitFormat.size() - 1;
		for (int i = 0; i < posOfNewCS; i++)
		{
			if (bestIndexI > bestIndexJ)
			{
				PL[i].erase(PL[i].begin() + bestIndexI);
				PL[i].erase(PL[i].begin() + bestIndexJ);
			}
			else
			{
				PL[i].erase(PL[i].begin() + bestIndexJ);
				PL[i].erase(PL[i].begin() + bestIndexI);
			}
			PL[i].resize(optimalCSInBitFormat.size());
			
			PL[i][posOfNewCS] = lf(optimalCSInBitFormat[i], optimalCSInBitFormat[posOfNewCS]);
		}

		PL[posOfNewCS].resize(optimalCSInBitFormat.size());
		for (int j = 0; j < posOfNewCS; j++)
			PL[posOfNewCS][j] = lf(optimalCSInBitFormat[posOfNewCS], optimalCSInBitFormat[j]);

		PL[posOfNewCS][posOfNewCS] = -std::numeric_limits<double>::infinity();

		bestPairValue = -10;

		int optimalCSInBitFormatSize = (int)optimalCSInBitFormat.size();

		// Update best indexes and best value of linkage, according to group size limitations
		for (int i = 0; i < optimalCSInBitFormatSize; i++)
			for (int j = 0; j < optimalCSInBitFormatSize; j++)
			{
				if (i == j)
					continue;

				unsigned int newPossibleCSSize = General::getSizeOfCombinationInBitFormat(optimalCSInBitFormat[i] ^ optimalCSInBitFormat[j]);
				if (newPossibleCSSize > maxNumberOfPlayersPerGroup)
					continue;

				coalitionsCanBeMerged = true;
				if (PL[i][j] > bestPairValue)
				{
					bestIndexI = i;
					bestIndexJ = j;
					bestPairValue = PL[i][j];
				}
			}
	}

	if (!coalitionsCanBeMerged)
		finalize();

	/*for (int i = 0; i < optimalCSInBitFormat.size(); i++)
		printf("%d ", optimalCSInBitFormat[i]);

	printf("\n");*/
}

void CLink::initializePL()
{
	for (unsigned int i = 0; i < numPlayers; i++)
		for (unsigned int j = 0; j < numPlayers; j++)
		{
			if (j == i)
				PL[i][j] = -std::numeric_limits<double>::infinity();
			else
				PL[i][j] = lf(optimalCSInBitFormat[i], optimalCSInBitFormat[j]);
		}
}


// Gain Link function
double CLink::lf(int coalition1, int coalition2)
{
	return coalitionValues[coalition1 ^ coalition2] - coalitionValues[coalition1] - coalitionValues[coalition2];
}


// Redistribute remaining coalitions in case not all coalitions respect players per group limitations
void CLink::finalize()
{
	// for (int i = 0; i < optimalCSInBitFormat.size(); i++)
	// {
	// 	printf("{%ld,%f}, \n", optimalCSInBitFormat[i], coalitionValues[optimalCSInBitFormat[i]]);
	// }
	// printf("\n----------\n");
	
	std::vector<long> smallCoalitions = std::vector<long>();
	for (int i = 0; i < optimalCSInBitFormat.size(); i++)
	{
		// find coalition with lower number of players than min number of players
		if (General::getSizeOfCombinationInBitFormat(optimalCSInBitFormat[i]) < minNumberOfPlayersPerGroup) 
		{
			smallCoalitions.push_back(optimalCSInBitFormat[i]);
			std::vector<long>::iterator it = optimalCSInBitFormat.begin() + i;
			optimalCSInBitFormat.erase(it);
		}
	}

	
	if (!smallCoalitions.empty())
	{
		std::vector<long> optimalCSInBitFormatCpy = std::vector<long>(optimalCSInBitFormat);
		for(int smallI=0; smallI < smallCoalitions.size(); smallI++){
			long smallCoalition = smallCoalitions[smallI];
			for(int mask = 1; mask <= smallCoalition; mask <<= 1){
				// printf("%d,", mask);
				if((mask & smallCoalition) == 0)
					continue;
				
				int indexOfBestCoalition = -1;
				double tempBestValue = -1;
				for (int i = 0; i < optimalCSInBitFormatCpy.size(); i++)
				{
					long modifiedCoalition = optimalCSInBitFormatCpy[i] ^ mask;
					double value = coalitionValues[modifiedCoalition];
					// printf("{%ld,%ld,%f}, \n", optimalCSInBitFormatCpy[i], mask, value);
					if (value >= tempBestValue)
					{
						tempBestValue = value;
						indexOfBestCoalition = i;
					}
				}
				optimalCSInBitFormat[indexOfBestCoalition] = optimalCSInBitFormat[indexOfBestCoalition] ^ mask;
			}
		}
		// printf("\n");
		// for (int i = 0; i < optimalCSInBitFormat.size(); i++)
		// {
		// 	printf("{%ld}, \n", optimalCSInBitFormat[i]);
		// }
		// printf("\n==========\n");
		
	}

}
