import React,{useState} from 'react'
import Select from 'react-select';

const options = [
    { value: 'chocolate', label: 'Chocolate' },
    { value: 'strawberry', label: 'Strawberry' },
    { value: 'vanilla', label: 'Vanilla' }

]

const SearchForm = () => {

    const [clearable,setClearable] = useState(true)

    const toggleClearable = () =>{setClearable(!clearable)}


    return (
        <div class="search-form">
                    <form>
                        <div className="">
                           
                                <div className="column">
                                <Select
                                className="mt-3"
                                classNamePrefix="Специалист"
                                isClearable={clearable}
                                placeholder={'Специалист'}
                                name="specialist"
                                options={options}/>
                                </div>
                        
                                <div className="column">

                                <Select
                                className="mt-3"
                                classNamePrefix="Специалист"
                                isClearable={clearable}
                                placeholder={'Град'}
                                name="specialist"
                                options={options}/>
                                </div>

                                <div className="column">
                                    <button className="mt-3">Търси</button>
                                </div>
                            </div>
                        
                    </form>
                </div>
    )
}

export default SearchForm
