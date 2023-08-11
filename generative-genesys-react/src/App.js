import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [creature_description, setCreatureDescription] = useState('');
  const [creature_name, setCreatureName] = useState('');
  const [creature_type, setCreatureType] = useState('');
  const [setting_description, setSettingDescription] = useState('A generic fantasy setting.');
  const [setting_specific_skills, setSettingSpecificSkills] = useState('');
  const [setting_removed_skils, setRemovedSkills] = useState('');
  const [skills, setSkills] = useState('');
  const [allow_other_skills, setAllowOtherSkills] = useState('');
  const [combat_cr, setCombatCR] = useState('');
  const [social_cr, setSocialCR] = useState('');
  const [general_cr, setGeneralCR] = useState('');
  const [brawn, setBrawn] = useState('');
  const [agility, setAgility] = useState('');
  const [intellect, setIntellect] = useState('');
  const [cunning, setCunning] = useState('');
  const [willpower, setWillpower] = useState('');
  const [presence, setPresence] = useState('');
  const [number_of_weapons, setNumberOfWeapons] = useState('');
  const [number_of_abilities, setNumberOfAbilities] = useState('');
  const [number_of_talents, setNumberOfTalents] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
    try {
      const result = await axios.post('http://localhost:5000/submit', { creature_description, creature_name, creature_type, setting_description, setting_specific_skills, setting_removed_skils, skills, allow_other_skills, combat_cr, social_cr, general_cr, brawn, agility, intellect, cunning, willpower, presence, number_of_weapons, number_of_abilities, number_of_talents });
      setResponse(result.data);
    } catch (err) {
      console.error('Error:', err);
      setResponse({ text: 'An error occurred' });
    }
  };

  return (
    <div>
      <input
        value={creature_description}
        onChange={(e) => setCreatureDescription(e.target.value)}
        placeholder="Creature Description"
        required
      />
      <input
        value={creature_name}
        onChange={(e) => setCreatureName(e.target.value)}
        placeholder="Creature Name"
        required
      />
      <select value={creature_type} onChange={(e) => setCreatureType(e.target.value)}>
          <option value="" disabled>Select a Creature Type</option>
          <option value="Minion">Minion</option>
          <option value="Rival">Rival</option>
          <option value="Nemesis">Nemesis</option>
      </select>
      <input
        value={setting_description}
        onChange={(e) => setSettingDescription(e.target.value)}
        placeholder="Setting Description"
      />
      <input
        value={setting_specific_skills}
        onChange={(e) => setSettingSpecificSkills(e.target.value)}
        placeholder="Setting Specific Skills"
      />
      <input
        value={setting_removed_skils}
        onChange={(e) => setRemovedSkills(e.target.value)}
        placeholder="Setting Removed Skills"
      />
      <input
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
        placeholder="Skills"
        required
      />
      <select value={allow_other_skills} onChange={(e) => setAllowOtherSkills(e.target.value)}>
          <option value="" disabled>Allow other skills than specified?</option>
          <option value="true">Yes</option>
          <option value="false">No</option>
      </select>
      <input
        value={combat_cr}
        onChange={(e) => setCombatCR(e.target.value)}
        placeholder="Combat CR"
      />
      <input
        value={social_cr}
        onChange={(e) => setSocialCR(e.target.value)}
        placeholder="Social CR"
      />
      <input
        value={general_cr}
        onChange={(e) => setGeneralCR(e.target.value)}
        placeholder="General CR"
      />
      <input
        value={brawn}
        onChange={(e) => setBrawn(e.target.value)}
        placeholder="Brawn"
      />
      <input
        value={agility}
        onChange={(e) => setAgility(e.target.value)}
        placeholder="Agility"
      />
      <input
        value={intellect}
        onChange={(e) => setIntellect(e.target.value)}
        placeholder="Intellect"
      />
      <input
        value={cunning}
        onChange={(e) => setCunning(e.target.value)}
        placeholder="Cunning"
      />
      <input
        value={willpower}
        onChange={(e) => setWillpower(e.target.value)}
        placeholder="Willpower"
      />
      <input
        value={presence}
        onChange={(e) => setPresence(e.target.value)}
        placeholder="Presence"
      />
      <input
        value={number_of_weapons}
        onChange={(e) => setNumberOfWeapons(e.target.value)}
        placeholder="Number of Weapons"
      />
      <input
        value={number_of_abilities}
        onChange={(e) => setNumberOfAbilities(e.target.value)}
        placeholder="Number of Abilities"
      />
      <input
        value={number_of_talents}
        onChange={(e) => setNumberOfTalents(e.target.value)}
        placeholder="Number of Talents"
      />
      <button onClick={handleSubmit}>Submit</button>

      {response && response.data && (
    <div>
        <pre>{JSON.stringify(response.data, null, 2)}</pre>
    </div>
)}
    </div>
  );
}

export default App;
